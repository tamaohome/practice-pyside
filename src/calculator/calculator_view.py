# -*- coding: utf-8 -*-

from PySide6.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QSizePolicy,
)
from PySide6.QtCore import Qt


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_grid_layout = MainGridLayout(self.central_widget)

    @property
    def buttons(self) -> dict[str, "CalculatorButton"]:
        """CalculatorButtonの辞書を返す"""
        return self.main_grid_layout.buttons

    @property
    def display(self) -> "DisplayLineEdit":
        """ディスプレイのDisplayLineEditを返す"""
        return self.main_grid_layout.display


class DisplayLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumHeight(40)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        font = self.font()
        font.setPointSize(16)
        self.setFont(font)


class MainGridLayout(QGridLayout):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        # ディスプレイを生成
        self.display = DisplayLineEdit()
        self.addWidget(self.display, 0, 0, 1, 4)

        # ボタンを生成
        self.buttons = {
            "C": CalculatorButton("C"),
            "=": CalculatorButton("="),
            "+": CalculatorButton("+"),
            "-": CalculatorButton("-"),
            "*": CalculatorButton("*"),
            "/": CalculatorButton("/"),
            ".": CalculatorButton("."),
        }
        for i in range(10):
            self.buttons[str(i)] = CalculatorButton(str(i))

        # ボタンの配置を定義
        btn = self.buttons
        positions: list[list[CalculatorButton | None]] = [
            [btn["C"], btn["/"], btn["*"], btn["-"]],
            [btn["7"], btn["8"], btn["9"], btn["+"]],
            [btn["4"], btn["5"], btn["6"], None],
            [btn["1"], btn["2"], btn["3"], btn["="]],
            [btn["0"], None, btn["."], None],
        ]

        # ボタンをグリッドに設置
        for row, buttons_row in enumerate(positions):
            for col, button in enumerate(buttons_row):
                if button is None:
                    continue
                match button.text():
                    case "+" | "=":
                        row_span, col_span = (2, 1)
                    case "0":
                        row_span, col_span = (1, 2)
                    case _:
                        row_span, col_span = (1, 1)
                self.addWidget(button, row + 1, col, row_span, col_span)


class CalculatorButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setMinimumSize(60, 40)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        font = self.font()
        font.setPointSize(16)
        self.setFont(font)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
