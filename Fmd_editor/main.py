import sys

from PyQt6.QtWidgets import *

from fmd_editor.controllers.edior_controller import EditorController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    e = EditorController()
    e.view()

    sys.exit(app.exec())
    #  e =FmdCompiler()
    source_code = """@title: A Comprehensive Fitx Document Example

@author: The Document Generator Team

@section: Introduction to Advanced Features
@text: This document serves as a complete demonstration of all features and elements supported by the document generator. It includes rich text, various list types, and different data visualizations.
@list(UNORDERED):
Paragraphs with **bold** and *italic* text.
Headings of multiple levels.
Ordered and unordered lists.
Embedded tables for data display.
Dynamic graphs and charts.
Code blocks for showcasing snippets.
Mathematical equations.
Image embedding.

@section: Detailed Data & Visualization
@text: Here, we explore the integration of structured data and visuals into the document. The following table represents global sales data.
@table([Region, Q1 Sales, Q2 Sales, Q3 Sales, Q4 Sales, Total Units Sold, Annual Revenue ]):
[[North America, 1500, 1750, 1900, 2100, 7250, 3625000], [Europe, 1200, 1400, 1650, 1800, 6050, 3025000], [Asia-Pacific, 2500, 2600, 2750, 2900, 10750, 5375000]]
@text: Next, we have a bar chart representing monthly revenue and a pie chart for budget allocation. This demonstrates how dynamic data can be rendered directly into the document.
@graph(BAR, Monthly Sales Data):
(January, 10)
(February, 25)
(March, 30)
(April, 15)

@graph(PIE, Project Budget Allocation):
(Design, 25)
(Development, 45)
(Marketing, 20)
(Operations, 10)

@section: Code & Equations
@text: Code blocks are ideal for sharing programming snippets. The following shows a simple Python function:
@code: def generate_report(data):
    # This function processes data and returns a document.
    processed_data = preprocess(data)
    document = render(processed_data)
    return document
@text: We can also include complex mathematical equations, which are useful for scientific and technical documents.
@equation: E = mc^2

@section: Conclusion
@text: This document has showcased a wide range of features, from basic text and lists to advanced data visualizations and code blocks. This demonstrates the flexibility of the system to handle a variety of content types while maintaining a clean and structured format.
@text: Thank you for exploring this document. We are excited for you to create your own!

"""
# e.compile(source_code)
# with open("src.json", "w") as src_file:
#   json.dump(e.document.get_context(),src_file, indent=4)
