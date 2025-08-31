import ast  # Added this import for literal_eval
import json
import re
import urllib.parse
from fmd_editor.core.fitx_compiler.document import Document, Section, ListType, GraphType


class FmdCompiler:
    def __init__(self):
        self.document: Document = Document()
        self.currentSection: Section = Section("")  # Not used in the current code, but kept for consistency
        self.output: {str: str}
        self.converter: JsonToHtmlConverter
        self.tokens = {  # Corrected to use self.tokens
            "@title": self.handle_title,  # not yet added
            "@author": self.handle_author,  # not yet added
            "@section": self.handle_section,  # not yet added
            # "@container": self.handle_container,
            "@text": self.handle_text,
            "@blockquote": self.handle_blockquote,  # not yet added
            "@page_break": self.handle_page_break,  # not yet added
            "@heading": self.handle_heading,  # not yet added
            "@list": self.handle_list,  # not yet added
            "@code": self.handle_code,  # not yet added
            "@table": self.handle_table,
            "@image": self.handle_image,
            "@graph": self.handle_graph,  # not yet added
            "@equation": self.handle_equation,
        }

    def compile(self, src: str) -> str:
        self.document = Document()
        for tag, props, content in self._parse(src):
            if tag in self.tokens:
                self.tokens[tag](props, content)
            else:
                raise (f"Warning: Unrecognized token '{tag}' found.")
        self.converter = JsonToHtmlConverter(self.document.get_context())
        return self.converter.convert_to_html()


    def _parse(self, src) -> list:  # Corrected to return a list
        matches = re.findall(r"(@\w+)\s*(\(.*?\))?:\s*(.*?)(?=@|$)", src, re.DOTALL)
        formatted_output = []
        for match in matches:
            tag = match[0]
            raw_params = match[1]
            content = match[2].strip()

            if raw_params:
                params_list = [p.strip() for p in raw_params.strip('()').split(',')]
                params_tuple = tuple(params_list)
            else:
                params_tuple = ()

            formatted_output.append((tag, params_tuple, content))
        return formatted_output

    def handle_title(self, props, text_content):
        self.document.add_title(text_content)

    def handle_author(self, props, text_content):
        self.document.add_author(text_content)

    def handle_section(self, props, text_content):
        self.document.add_section(Section(text_content))

    def handle_text(self, props, text_content):
        # Corrected method to get the last section
        if self.document.get_last_section():
            self.document.get_last_section().addText(text_content)
        else:
            print("Warning: Text block outside of a section. Creating new section.")
            self.document.add_section(Section("Untitled Section"))
            self.document.get_last_section().addText(text_content)

    def handle_blockquote(self, props, element_data):
        self.document.get_last_section().addBlockquote(element_data)

    def handle_page_break(self, props, element_data):
        self.document.get_last_section().addPageBreak()

    def handle_heading(self, props, element_data):
        if not props or not props[0].isnumeric():
            level = 4
        else:
            level = int(props[0])
            if level > 4:
                level = 4  # Capped at 4

        self.document.get_last_section().addheading(level, text=element_data)

    def handle_list(self, props, element_data):
        # Corrected variable name from props[0] to props
        if props and props[0] == "ORDERED":
            self.document.get_last_section().addList(type=ListType.ORDERED, data=element_data.split('\n'))
        elif props and props[0] == "UNORDERED":
            self.document.get_last_section().addList(type=ListType.UNORDERED, data=element_data.split('\n'))
        else:
            # Better error message
            self.document.get_last_section().addText(
                f"Error: '{props[0] if props else 'None'}' is not a valid list type. Use ORDERED or UNORDERED.")

    def handle_code(self, props, element_data):
        self.document.get_last_section().addCode(element_data)

    def handle_table(self, props, element_data):
        try:
            self.document.get_last_section().addTable(headers=props, data=ast.literal_eval(
                re.sub(r'(\b[a-zA-Z\s-]+)\b', r"'\1'", element_data)))
        except (ValueError, SyntaxError) as e:
            self.document.get_last_section().addText(f"Error parsing the table:\n")

    def handle_image(self, props, element_data):
        print(props[0], props[1], props[2])
        try:
            if props[0] and len(props) == 3:
                self.document.get_last_section().addImage(props[0], props[1], props[2])
            else:
                raise ValueError("Image token requires at least 3 parameters: url, caption, alt_text")
        except Exception as e:
            self.document.get_last_section().addText(f"Error parsing the image element:\n{e}")

    def handle_graph(self, props, element_data):
        print(props, type(element_data))
        try:

            if props and props[0] == "PIE":
                output_list = {
                    "labels": [],
                    "data": []
                }
                for item in re.findall(r"\((.*?)\)", element_data):
                    parts = [part.strip() for part in item.split(',')]
                    if len(parts) == 2 and parts[1].strip().isnumeric():
                        output_list["labels"].append(parts[0].strip())
                        output_list["data"].append(int(parts[1].strip()))
                    else:
                        raise ValueError(f"Invalid format for data point: '{item}'")

                self.document.get_last_section().addPieGraph(type=GraphType.PIE, caption=props[1], data=output_list)
            elif props and props[0] == "BAR":
                output_list = {
                    "labels": [],
                    "datasets": []
                }
                output_list["datasets"].append({"label": props[2], "data": []})
                for item in re.findall(r"\((.*?)\)", element_data):
                    parts = [part.strip() for part in item.split(',')]
                    if len(parts) == 2 and parts[1].strip().isnumeric():
                        output_list["labels"].append(parts[0].strip())
                        output_list["datasets"][0]["data"].append(int(parts[1].strip()))

                    else:
                        raise ValueError(f"Invalid format for data point: '{item}'")
                self.document.get_last_section().addBarGraph(type=GraphType.BAR, caption=props[1], data=output_list)



            else:
                self.document.get_last_section().addText("Error: Invalid graph type. Use PIE or BAR.")

        except Exception as e:
            self.document.get_last_section().addText(f"Error parsing the graph:\n{e}")

    def handle_equation(self, props, element_data):
        self.document.get_last_section().addEquation(element_data)







class JsonToHtmlConverter:


    def __init__(self, json_data):

        self.data = json_data
        # Define default settings
        default_settings = {
            "document_background_color": "#f7fafc",
            "document_text_color": "#1a202c",
            "container_background_color": "#fff",
            "container_width_px": 800,
            "heading_color": "#2b6cb0",
            "link_color": "#2c5282",
            "code_background_color": "#f5f5f5",
        }

        # Merge user-provided settings with defaults
        user_settings = self.data.get("settings", {})
        self.settings = {**default_settings, **user_settings}

        #self.page_dimensions = {
     #       "A4": {"portrait": "21cm", "landscape": "29.7cm"},
     #       "A3": {"portrait": "29.7cm", "landscape": "42cm"},
     #   }

    def _get_css(self):
        """
        Generates the CSS as a string, using the settings to customize styles.
        All print-related CSS has been removed.
        """
        return f"""
        body {{
            font-family: 'Inter', sans-serif, 'Segoe UI', 'Roboto', 'Oxygen';
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: {self.settings['document_background_color']};
            color: {self.settings['document_text_color']};
            font-size: 16px;
            display: flex;
            justify-content: center;
        }}
        .document-container {{
            background-color: {self.settings['container_background_color']};
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin: 2rem;
            padding: 2.5rem;
            width: 100%;
            max-width: {self.settings['container_width_px']}px;
            box-sizing: border-box;
        }}
        .document-container > * {{
            max-width: 100%;
        }}
        .title-block {{
            text-align: center;
            margin-bottom: 3rem;
        }}
        .title {{
            font-size: 2.5rem;
            font-weight: 700;
            color: {self.settings['heading_color']};
            margin: 0;
        }}
        .author {{
            font-size: 1.25rem;
            color: #4a5568;
            margin-top: 5px;
        }}
        .section {{
            margin-bottom: 2.5rem;
        }}
        .section h2 {{
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            color: {self.settings['heading_color']};
            font-size: 2rem;
            font-weight: 700;
        }}
        .section h3 {{
            color: {self.settings['heading_color']};
            margin-top: 2rem;
            font-size: 1.5rem;
        }}
        p {{
            margin-bottom: 1rem;
            text-align: justify;
        }}
        a {{
            color: {self.settings['link_color']};
            text-decoration: none;
            border-bottom: 1px dashed;
        }}
        a:hover {{
            border-bottom-style: solid;
        }}
        ul, ol {{
            margin: 0 0 1rem 2rem;
        }}
        li {{
            margin-bottom: 0.5rem;
        }}
        pre.code {{
            background-color: {self.settings['code_background_color']};
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            font-family: 'Roboto Mono', monospace;
            border: 1px solid #e2e8f0;
            margin-bottom: 1rem;
        }}
        .equation {{
            text-align: center;
            margin: 1.5rem 0;
            font-style: italic;
        }}
        .table-container {{
            overflow-x: auto;
            margin: 1.5rem 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}
        th, td {{
            padding: 0.75rem 1rem;
            border: 1px solid #e2e8f0;
            text-align: left;
        }}
        th {{
            background-color: #f0f0f0;
            font-weight: bold;
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }}
        .figure, .graph, .image {{
            text-align: center;
            margin: 2rem 0;
        }}
        .caption {{
            font-size: 0.9rem;
            color: #4a5568;
            margin-top: 1rem;
        }}
        blockquote {{
            background-color: #f0f8ff;
            border-left: 4px solid #3182ce;
            margin: 1.5rem 0;
            padding: 1rem 1.5rem;
            font-style: italic;
        }}
        h3, h4, h5, h6 {{
            color: {self.settings['heading_color']};
        }}
        h3 {{ font-size: 1.5rem; }}
        h4 {{ font-size: 1.25rem; }}
        h5 {{ font-size: 1rem; }}
        h6 {{ font-size: 0.8rem; }}
        """

    def _get_chart_config(self, graph_type, graph_data):
        """
        Generates the Chart.js JSON configuration string for different graph types.
        Fixes the chart rendering bug by ensuring the JSON is valid before URL encoding.
        """
        config = {
            "type": graph_type,
            "data": {
                "labels": graph_data.get("labels", []),
                "datasets": graph_data.get("datasets", [])
            },
            "options": {
                "plugins": {"legend": {"display": True}}
            }
        }

        if graph_type == "bar" and isinstance(graph_data.get("datasets"), dict):
            config["data"]["datasets"] = [graph_data.get("datasets")]
        elif graph_type in ["pie", "doughnut"]:
            config["data"]["datasets"] = [{
                "data": graph_data.get("data", []),
                "backgroundColor": graph_data.get("backgroundColor", ["#FF6384", "#36A2EB", "#FFCE56", "#E7E9ED"])
            }]
            config["data"]["labels"] = graph_data.get("labels", [])

        json_string = json.dumps(config)
        return urllib.parse.quote_plus(json_string)

    def _render_graph(self, graph_data):
        """
        Renders a graph by generating a static image via a service like QuickChart.io.
        """
        graph_type = graph_data.get("graph_type", "bar")
        chart_config = self._get_chart_config(graph_type, graph_data.get("data", {}))

        src = f"https://quickchart.io/chart?width=600&height=400&c={chart_config}"

        return f"""
        <div class="graph">
            <img src="{src}" alt="{graph_data.get('alt', 'A chart or graph.')}" />
            <p class="caption">{graph_data.get('caption', '')}</p>
        </div>
        """

    def _markdown_to_html(self, text):
        """
        Converts a simple markdown subset to HTML.
        Supports bold (**text** or __text__) and italic (*text* or _text_).
        """
        text = re.sub(r'\\n', '<br>', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
        return text

    def _render_item(self, item):
        """
        Helper function to render a single content item.
        """
        if not isinstance(item, dict):
            return ""

        item_type = item.get('type')

        match item_type:
            case 'paragraph' | 'text':
                text_content = item.get("text", item.get("content", ""))
                # Check for a markdown content key first, then a regular content key.
                # Convert markdown to HTML before adding to the document.
                if "markdown_content" in item:
                    text_content = item["markdown_content"]
                    html_content = self._markdown_to_html(text_content)
                    return f'<p>{html_content}</p>\n'

                html_content = self._markdown_to_html(text_content)
                return f'<p>{html_content}</p>\n'

            case 'list':
                list_type = item.get('list_type', 'unordered')
                tag = 'ul' if list_type == 'unordered' else 'ol'
                list_html = f'<{tag}>\n'
                for li in item.get('items', []):
                    list_html += f'<li>{self._markdown_to_html(li)}</li>\n'
                list_html += f'</{tag}>\n'
                return list_html

            case 'equation':
                equation_content = re.sub(r'\$+', '', item.get("content", ""))
                return f'<p class="equation">$$ {equation_content} $$</p>\n'

            case 'table':
                table_html = '<div class="table-container">\n<table>\n<thead>\n<tr>\n'
                for header in item.get('headers', []):
                    table_html += f'<th>{header}</th>\n'
                table_html += '</tr>\n</thead>\n<tbody>\n'
                for row in item.get('data', []):
                    table_html += '<tr>\n'
                    for cell in row:
                        table_html += f'<td>{cell}</td>\n'
                    table_html += '</tr>\n'
                table_html += '</tbody>\n</table>\n</div>\n'
                return table_html

            case 'image':
                html = f'<div class="image">\n'
                html += f'<img src="{item.get("src")}" alt="{item.get("alt", "")}">\n'
                if item.get("caption"):
                    html += f'<p class="caption">{self._markdown_to_html(item.get("caption"))}</p>\n'
                html += f'</div>\n'
                return html

            case 'link':
                return f'<p><a href="{item.get("href", "")}">{self._markdown_to_html(item.get("text", ""))}</a></p>\n'

            case 'code':
                return f'<pre class="code">{item.get("content", "")}</pre>\n'

            case 'blockquote':
                return f'<blockquote>{self._markdown_to_html(item.get("text", ""))}</blockquote>\n'

            case 'heading':
                level = item.get("level", 4)
                return f'<h{level}>{self._markdown_to_html(item.get("text", ""))}</h{level}>\n'

            case 'divider':
                return '<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 2rem 0;">\n'

            case 'graph':
                return self._render_graph(item)

            case _:
                return ""

    def convert_to_html(self):
        """
        The main function to perform the conversion.
        Now correctly handles page breaks by building pages incrementally.
        """
        if not self.data or not self.data.get('sections'):
            return "<html><body><h1>Error: No data provided.</h1></body></html>"

        sections_html = []

        # Add the title block
        sections_html.append('<div class="title-block"><h1 class="title">' + self.data.get("title",
                                                                                           "Document Title") + '</h1><p class="author">' + self.data.get(
            "author", "Unknown Author") + '</p></div>\n')

        # Process each section and its content
        for section in self.data.get('sections', []):
            sections_html.append(f'<div class="section">\n')
            sections_html.append(f'<h2>{self._markdown_to_html(section.get("heading", "Untitled Section"))}</h2>\n')

            for item in section.get('content', []):
                sections_html.append(self._render_item(item))

            sections_html.append('</div>\n')

        full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.data.get('title', 'Document')}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Lora:ital,wght@0,400..700;1,400..700&family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        {self._get_css()}
    </style>
</head>
<body>
    <div class="document-container">
        {"".join(sections_html)}
    </div>
</body>
</html>
        """
        return full_html
