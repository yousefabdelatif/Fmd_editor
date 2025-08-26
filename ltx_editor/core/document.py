from enum import Enum
from pathlib import Path
from itx_compiler.tokens.Formats import Elements


class PageSize(Enum):
    a4 =(21.0, 29.7)
    a3 =(29.7, 42.0)


class PageOriantation(Enum):
    VERTICAL :0
    HORIZONATAL: 1
class ContainerType(Enum):
    FLEXABLE :0
    SIZED: 1
    CONST_SIZE:2

class GraphType(Enum):
    BAR = "bar"
    PIE = "pie"


class ListType(Enum):
    ORDERED = "ordered"
    UNORDERED = "unordered"
class TextType(Enum):
    TTILE = "ordered"
    SUBTITLE = "unordered"
    TEXT = "unordered"
    QOUTE = "qoute"


class Section:
    def __init__(self, heading: str):
        self.heading = heading
        self.data = []

    def addEquation(self, text: str):
        self.data.append({
            "type": "equation",
            "content": text
        })

    def addBlockquote(self, text: str):
        self.data.append({
            "type": "blockquote",
            "text": text
        })

    def addtext(self, tyoe: TextType, text: str):
        self.data.append({
            "type": "heading",
            "level": level,
            "text": text
        })

    def addText(self, text: str):
        self.data.append({
            "type": "text",
            "content": text
        })

    def addPageBreak(self):
        self.data.append({
            "type": "page_break"
        })

    def addTable(self, headers: list[str], data: list):
        self.data.append({
            "type": "table",
            "headers": headers,
            "data": data
        })

    def addPieGraph(self, type: GraphType, caption: str, data: dict):

        self.data.append({
            "type": "graph",
            "graph_type": "pie",
            "caption": caption,
            "data": data
        })

    def addBarGraph(self, type: GraphType, caption: str, data: dict):

        self.data.append({
            "type": "graph",
            "graph_type": "bar",
            "caption": caption,
            "data": data
            })
    def addList(self, type: ListType, data: list):
        self.data.append({
            "type": "list",
            "list_type": type.value,
            "items": data
        })

    def addImage(self, src: str, alt: str = "", caption: str = ""):
        self.data.append({
            "type": "image",
            "src": src,
            "alt": alt,
            "caption": caption
        })

    def addCode(self, text: str):
        self.data.append({
            "type": "code",
            "content": text
        })


    def getData(self):
        return {
            "heading": "Code & Equations",
            "content": self.data

        }

class Document:
    def __init__(self):
        self._title = ""
        self._author = ""
        self._last_section = None
        self._sections = []
        self._settings =  {}

    def add_section(self, section:Section):
        # If there's a previous section, save its data to the list
        if self._last_section:
            self._sections.append(self._last_section.getData())
        # Set the new section as the current last section
        self._last_section = section

    def add_title(self, title: str):
        self._title = title

    def add_author(self, author: str):
        self._author = author

    def get_last_section(self) -> 'Section':
        if self._last_section is None:
            # Create a default section if none exists
            self._last_section = Section("Default Section")
        return self._last_section

    def get_context(self) -> dict:
        # Append the last section's data before returning the full context
        if self._last_section:
            self._sections.append(self._last_section.getData())
            self._last_section = None  # Reset the last section pointer

        return {
            "title": self._title,
            "author": self._author,
            "settings": self._settings,
            "sections": self._sections
        }


class Section:
    def __init__(self, heading: str):
        self.heading = heading
        self.data = []

    def addEquation(self, text: str):
        self.data.append({
            "type": "equation",
            "content": text
        })

    def addBlockquote(self, text: str):
        self.data.append({
            "type": "blockquote",
            "text": text
        })

    def addtext(self, tyoe: TextType, text: str):
        self.data.append({
            "type": "heading",
            "level": level,
            "text": text
        })

    def addText(self, text: str):
        self.data.append({
            "type": "text",
            "content": text
        })

    def addPageBreak(self):
        self.data.append({
            "type": "page_break"
        })

    def addTable(self, headers: list[str], data: list):
        self.data.append({
            "type": "table",
            "headers": headers,
            "data": data
        })

    def addPieGraph(self, type: GraphType, caption: str, data: dict):

        self.data.append({
            "type": "graph",
            "graph_type": "pie",
            "caption": caption,
            "data": data
        })

    def addBarGraph(self, type: GraphType, caption: str, data: dict):

        self.data.append({
            "type": "graph",
            "graph_type": "bar",
            "caption": caption,
            "data": data
            })
    def addList(self, type: ListType, data: list):
        self.data.append({
            "type": "list",
            "list_type": type.value,
            "items": data
        })

    def addImage(self, src: str, alt: str = "", caption: str = ""):
        self.data.append({
            "type": "image",
            "src": src,
            "alt": alt,
            "caption": caption
        })

    def addCode(self, text: str):
        self.data.append({
            "type": "code",
            "content": text
        })


    def getData(self):
        return {
            "heading": self.heading,
            "content": self.data

        }





