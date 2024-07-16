import sys
from pathlib import Path

from typing import Optional

from PySide6.QtCore import Slot, QFile, QTextStream
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QHBoxLayout
)

from preview_window import PreviewWindow
from drag_drop_widget import DragDropWidget
from title_label import TitleLabel
from edl_to_yt import string_from_path


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.drag_drop_widget = None
        self.preview_widget = None

        self.preview_button = None
        self.save_button = None

        self.input_path: Optional[Path] = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('EDL Convert')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        central_widget.setLayout(layout)

        layout.addWidget(TitleLabel('Upload file', self))

        self.drag_drop_widget = DragDropWidget(self)
        layout.addWidget(self.drag_drop_widget)

        choose_deselect_file_layout = QHBoxLayout()
        layout.addLayout(choose_deselect_file_layout)

        choose_input_file_button = QPushButton('Choose File', self)
        choose_input_file_button.clicked.connect(self.open_input_file_dialog)
        choose_deselect_file_layout.addWidget(choose_input_file_button)

        deselect_file_button = QPushButton('Deselect File', self)
        deselect_file_button.clicked.connect(self.deselect_file)
        choose_deselect_file_layout.addWidget(deselect_file_button)

        layout.addWidget(TitleLabel('Select output', self))

        preview_save_layout = QHBoxLayout()
        layout.addLayout(preview_save_layout)

        self.preview_button = QPushButton('Preview', self)
        self.preview_button.clicked.connect(self.open_preview)
        self.preview_button.setDisabled(True)
        preview_save_layout.addWidget(self.preview_button)

        self.save_button = QPushButton('Save as text', self)
        self.save_button.setDisabled(True)
        self.save_button.clicked.connect(self.save_to_file)
        preview_save_layout.addWidget(self.save_button)

        self.show()

    def open_input_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "EDL Files (*.edl)", options=options)
        if file_name:
            self.on_file_uploaded(file_name)

    def save_to_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)", options=options)
        if file_name:
            file = QFile(file_name)
            if file.open(QFile.WriteOnly | QFile.Text):
                text_stream = QTextStream(file)
                text_stream << string_from_path(self.input_path)
                file.close()

    def open_preview(self):
        string_value = string_from_path(self.input_path)
        self.preview_widget = PreviewWindow(string_value)

    @Slot(str)
    def on_file_uploaded(self, file_path: str):
        self.drag_drop_widget.label.setText(f"Selected file: {file_path}")
        self.input_path: Path = Path(file_path)

        self.preview_button.setDisabled(False)
        self.save_button.setDisabled(False)

    def deselect_file(self):
        self.preview_button.setDisabled(True)
        self.save_button.setDisabled(True)
        self.input_path = None
        self.drag_drop_widget.label.setText("Drag and drop a file here or click 'Choose File' to select a file")


def main():
    app = QApplication(sys.argv)

    _ = App()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
