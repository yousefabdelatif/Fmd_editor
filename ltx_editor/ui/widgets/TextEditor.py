import sys
from PyQt6.QtCore import Qt
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.Qsci import QsciLexerCustom, QsciAPIs, QsciScintilla
from PyQt6.QtGui import QColor, QFont


# =========================================================================
# The Custom Lexer for Syntax Highlighting
# =========================================================================
class CustomLexer(QsciLexerCustom):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setDefaultFont(QFont("Courier New", 10))
        self.setDefaultPaper(QColor("#FFFFFF"))

        # Define styles for your custom tags
        self.tag_style = 0  # e.g., <doc>, </doc>
        self.special_tag_style = 1 # e.g., @title:, @image():
        self.default_style = 2  # A style for all other text

        self.setColor(QColor(Qt.GlobalColor.darkBlue), self.tag_style)
        self.setFont(QFont("Courier New", 10, QFont.Weight.Bold), self.tag_style)

        self.setColor(QColor(Qt.GlobalColor.darkMagenta), self.special_tag_style)
        self.setFont(QFont("Courier New", 10, QFont.Weight.Bold), self.special_tag_style)

        self.setColor(QColor(Qt.GlobalColor.black), self.default_style)
        self.setFont(QFont("Courier New", 10), self.default_style)

        # Updated regex to match all tags from your list, including the colon
        self.combined_pattern = re.compile(
            r'(?P<html_tags><[a-z/]+>)|(?P<special_tags>@\w+(?:\(.*?\)|\{.*?\}|):)',
            re.DOTALL
        )

    def language(self):
        return "Custom Language"

    def description(self, style):
        if style == self.tag_style:
            return "HTML Tags"
        if style == self.special_tag_style:
            return "Special Tags"
        if style == self.default_style:
            return "Default"
        return ""

    def styleText(self, start, end):
        editor = self.parent()
        text = editor.text()[start:end]
        self.startStyling(start)
        current_pos = 0

        for match in self.combined_pattern.finditer(text):
            plain_text_len = match.start() - current_pos
            if plain_text_len > 0:
                self.setStyling(plain_text_len, self.default_style)

            if match.group('html_tags'):
                style = self.tag_style
            elif match.group('special_tags'):
                style = self.special_tag_style
            else:
                style = self.default_style

            token_length = match.end() - match.start()
            self.setStyling(token_length, style)
            current_pos = match.end()

        if current_pos < len(text):
            self.setStyling(len(text) - current_pos, self.default_style)


# =========================================================================
# The Editor Widget with Autocompletion
# =========================================================================
class Editor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)

        lexer = CustomLexer(self)
        self.setLexer(lexer)

        # Autocompletion setup
        self.api = QsciAPIs(lexer)
        # Updated word list to match the tags with colons
        word_list = [
            "@title:",
            "@author:",
            "@section:",
            "@image():",
            "@text:",
            "@list():",
            "@table():",
            "@graph():",
            "@graph():",
            "@code:",
            "@equation:",
        ]
        for word in word_list:
            self.api.add(word)
        self.api.prepare()

        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAPIs)
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionUseSingle(QsciScintilla.AutoCompletionUseSingle.AcusNever)
        self.setAutoCompletionThreshold(1)

        # Other editor settings
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, "99999")
        self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
        self.setCaretForegroundColor(QColor(Qt.GlobalColor.black))

