from PySide6.QtWidgets import QLabel

from fonts import TitleFont


class TitleLabel(QLabel):
    def __init__(self, title: str, parent = None):
        super().__init__(parent)
        self.setText(title)
        self.setFont(TitleFont())

        height = 40

        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
