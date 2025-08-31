
## FMD: A Comprehensive Document Scripting Language

-----

FMD is a powerful and flexible scripting language designed for generating rich, structured documents. It allows you to define content, layout, and even data visualizations in a simple, human-readable format.

### Core Features

  * **Structured Sections:** Organize your document using clear, hierarchical sections.
  * **Rich Text Formatting:** Easily apply **bold** and *italic* formatting to text.
  * **Lists:** Create both ordered and unordered lists for structured information.
  * **Data Integration:** Embed tables and dynamic charts (bar and pie charts) to visualize data directly within your document.
  * **Code Blocks:** Include formatted code snippets for technical documentation.
  * **Mathematical Equations:** Render complex mathematical formulas.
  * **Metadata:** Define document title and author information.
  * **Image Embedding:** Include images directly from a URL.

### Syntax Reference

The FMD language uses a simple `@` syntax to define different content types. Each command starts with `@` followed by a keyword, and often includes arguments in parentheses `()`.

#### Document Metadata

  * `@title: [Document Title]` - Defines the title of the document.
  * `@author: [Author Name]` - Specifies the author of the document.

#### Sections

  * `@section: [Section Title]` - Creates a new document section with a specified title.

#### Text and Formatting

  * `@text: [Your Text Here]` - Inserts a paragraph of text. You can use `**` for **bold** and `*` for *italic* text.

#### Lists

  * `@list(ORDERED):` - Creates an ordered (numbered) list.
  * `@list(UNORDERED):` - Creates an unordered (bulleted) list.
  * Following the list declaration, each item should be on a new line.

#### Tables

  * `@table([Column 1, Column 2, ...]):` - Starts a new table. The argument is an array of column headers.
  * The data for the table should be provided in a nested array format, with each inner array representing a row: `[[Row 1 Data], [Row 2 Data]]`.

#### Graphs and Charts

  * `@graph(BAR, [Chart Title],[Data Title]):` - Generates a **bar chart**.
  * `@graph(PIE, [Chart Title]):` - Generates a **pie chart**.
  * The data for graphs is provided as a series of `(Label, Value)` pairs, each on a new line.

#### Code and Equations

  * `@code:` - Begins a code block. The code should be on the following lines and will be displayed with monospaced formatting.
  * `@equation: [Equation]` - Renders a mathematical equation. The equation should be written in a standard mathematical notation.

#### Images

  * `@image([Image URL]):` - Embeds an image directly from the provided URL.

-----

### Example

Here is a simple example of how to use FMD to create a document with a heading, some text, a list, and a small table.

```
@title: A Comprehensive FMD Document

@author: The Document Generator Teamk

@section: Introdsuctio to Avanced Features
@image (https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_16x9.jpg?w=1200,h,h):

@text: This document serves as a complete demonstration of all features and elements supported by the document generator. 

It includes amzdklsd;s text, various list types, and data visualizations.
@text:fsa
@list(ORDERED):
Paragraphs with **bold** and *italic* text.
Headings of multiple levels.j
Ordered and unozzrdered lists.
Embedded tables for data display.
Dynamic graphs and charts.
Code blocks for showcasing snippefts
Mathematical equayiodnss.
Image embedding.

@text: Herje, we explore the integration of strusctured data and visuals into the document. The following table represents global sales data.
@table(Region, Q1 Sales, Q2 Sales, Q3 Sales, Q4 Sales, Total Units Sold, Annual Revenue):
[[North America, 1500, 1750, 1900, 2100, 7250, 3625000], [Europe, 1200, 1400, 1650, 1800, 6050, 3025000], [Asia-Pacific, 2500, 2600, 2750, 2900, 10750, 5375000]]
@text: Next, we have a bar chart represaenting monthly revenue and a pie chart for budget allocation. This demonstrates how dynamic data can be rendered directly into the document.
@graph(BAR, Monthly Sales Data,Revenue):
(January, 10)
(February, 25)
(March, 30)
(April, 15)


@graph(PIE, Project Budget Allocation):
(Design, 20)
(Development, 50)
(Marketing, 40)
(Operations, 10)

@section: Code & Equationsd
@text: Code blocks are ideal for sharing programming snippets. The following shows a simple Python function:
@code: def generate_report(data):
    # This function processes data and returns a document.
    processed_data = preprocess(data)
    document = render(processed_daa)
    return document



@text: We can also include complex mathematical equations, which are useful for scientific and technical documents.

@equation: e^{i\theta} = \int_{0}^{\infty} \frac{\sin(x)}{x} dx + \sum_{n=1}^{\infty} \frac{1}{n^2} - \sqrt[3]{8} + \frac{i\pi}{2}

@section: Conclusion

@text: This document has showcased a wide range of features, from basic text and lists to advanced data visualizations and code blocks. This demonstrates the flexibility of the system to handle a variety of content types while maintaining a clean and structure
@text: We can also include complex mathematical equations, which are useful for scientific and technical documents.

```
