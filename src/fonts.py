from PySide6.QtGui import QFont


class TitleFont(QFont):
    def __init__(self):
        super().__init__()
        self.setPointSize(16)
        self.setBold(True)


class TextFont(QFont):
    def __init__(self):
        super().__init__()
        self.setPointSize(10)
