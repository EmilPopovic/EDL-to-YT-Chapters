from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

from fonts import TextFont


class PreviewWindow(QWidget):
    def __init__(self, content: str, parent=None):
        super().__init__()

        self.content = content

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Output preview")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

        text_edit = QTextEdit(self)
        text_edit.setPlainText(self.content)
        text_edit.setFont(TextFont())
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

        self.show()
