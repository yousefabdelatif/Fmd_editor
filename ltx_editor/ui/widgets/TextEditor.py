from PyQt6.QtCore import Qt
import re
from PyQt6.Qsci import QsciLexerCustom, QsciAPIs
from PyQt6.Qsci import QsciScintilla
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt
import re
from PyQt6.Qsci import QsciLexerCustom, QsciAPIs
from PyQt6.Qsci import QsciScintilla
from PyQt6.QtGui import QColor, QFont


# =========================================================================
# The Custom Lexer for Syntax Highlighting (DEFINE THIS FIRST)
# =========================================================================
class CustomLexer(QsciLexerCustom):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Default font and colors
        self.setDefaultFont(QFont("Courier New", 10))
        self.setDefaultPaper(QColor("#FFFFFF"))

        # Define styles for your custom tags
        self.tag_style = 0
        self.special_tag_style = 1
        self.default_style = 2  # A style for all other text

        # Set the styling for each style number
        # Tag style: e.g., <doc>, </doc>
        self.setColor(QColor(Qt.GlobalColor.darkBlue), self.tag_style)
        self.setFont(QFont("Courier New", 10, QFont.Weight.Bold), self.tag_style)

        # Special tag style: e.g., @image(), @table{}
        self.setColor(QColor(Qt.GlobalColor.darkMagenta), self.special_tag_style)
        self.setFont(QFont("Courier New", 10, QFont.Weight.Bold), self.special_tag_style)

        # Default text style
        self.setColor(QColor(Qt.GlobalColor.black), self.default_style)
        self.setFont(QFont("Courier New", 10), self.default_style)

        # Combine all patterns into a single regex for efficient parsing
        # The | (OR) operator is used to match any of the patterns
        # The ?P<name> is used to create named groups for easier identification
        # of the matched pattern.
        self.combined_pattern = re.compile(
            r'(?P<tag><[a-z]+>)|(?P<closing_tag></[a-z]+>)|(?P<special_image>@image\(.*?\))|(?P<special_table>@table\{.*?\})|(?P<special_link>@link\(\))',
            re.DOTALL
        )

    def language(self):
        return "Custom Language"

    def description(self, style):
        if style == self.tag_style:
            return "Tags"
        if style == self.special_tag_style:
            return "Special Tags"
        if style == self.default_style:
            return "Default"
        return ""

    def styleText(self, start, end):
        # The text to style is a slice of the full document text
        editor = self.parent()
        text = editor.text()[start:end]

        # Start styling from the given 'start' position
        self.startStyling(start)

        # Keep track of the current position in the text slice
        current_pos = 0

        # Use finditer to find all matches in the text slice
        for match in self.combined_pattern.finditer(text):
            # Style the plain text that came before the match
            plain_text_len = match.start() - current_pos
            if plain_text_len > 0:
                self.setStyling(plain_text_len, self.default_style)

            # Now, determine which pattern matched and apply the correct style
            if match.group('tag') or match.group('closing_tag'):
                style = self.tag_style
            elif match.group('special_image') or match.group('special_table') or match.group('special_link'):
                style = self.special_tag_style
            else:
                # Should not happen with the current regex, but good practice
                style = self.default_style

            # Style the matched token itself
            token_length = match.end() - match.start()
            self.setStyling(token_length, style)

            # Update the current position
            current_pos = match.end()

        # Style any remaining plain text at the end of the text slice
        if current_pos < len(text):
            self.setStyling(len(text) - current_pos, self.default_style)


# =========================================================================
# The Editor Widget (USES the CustomLexer)
# =========================================================================
class Editor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Now this line works because CustomLexer is already defined
        lexer = CustomLexer(self)
        self.setLexer(lexer)

        # ... (rest of the Editor class code) ...
        self.api = QsciAPIs(lexer)
        word_list = ["<doc>", "</doc>", "<page>", "</page>", "@image()", "@table{}", "@link()"]
        for word in word_list:
            self.api.add(word)
        self.api.prepare()

        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAPIs)
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionUseSingle(QsciScintilla.AutoCompletionUseSingle.AcusNever)
        self.setAutoCompletionThreshold(1)

        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, "99999")
        self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
        self.setCaretForegroundColor(QColor(Qt.GlobalColor.black))