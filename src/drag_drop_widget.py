from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel

from fonts import TextFont


class DragDropWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.text_edit = None
        self.label = None
        self.layout = None

        self.parent = parent


        self.setAcceptDrops(True)
        self.init_ui()

    def init_ui(self):
        self.setFrameStyle(QFrame.StyledPanel)

        self.setMinimumHeight(150)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Drag and drop a file here or click 'Choose File' to select a file", self)
        self.label.setFont(TextFont())
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            if file_path and file_path.split('.')[-1] == 'edl':
                event.acceptProposedAction()
            else:
                event.ignore()

    def dropEvent(self, event: QDropEvent):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.label.setText(f"Selected file: {file_path}")
        self.parent.on_file_uploaded(file_path)
