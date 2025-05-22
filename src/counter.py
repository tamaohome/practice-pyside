# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class CounterModel:
    def __init__(self):
        self._count = 0

    def increment(self) -> None:
        self._count += 1

    def reset_count(self) -> None:
        self._count = 0

    @property
    def count(self) -> int:
        return self._count


class CounterView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter")
        self.setFixedSize(160, 140)

        # 閉じるボタンのみ表示
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowCloseButtonHint)

        self.counter = CounterLineEdit()

        self.increment_button = QPushButton("Increment")
        self.reset_button = QPushButton("Reset")

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.counter)
        self.v_layout.addWidget(self.increment_button)
        self.v_layout.addWidget(self.reset_button)
        self.setLayout(self.v_layout)

    def set_count(self, num: int) -> None:
        self.counter.setText(str(num))


class CounterLineEdit(QLineEdit):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setText("0")
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.setFont(font)


class CounterController:
    def __init__(self, model: CounterModel, view: CounterView):
        self.model = model
        self.view = view
        self.view.increment_button.clicked.connect(self.increment_count)
        self.view.reset_button.clicked.connect(self.reset_count)

    def increment_count(self) -> None:
        self.model.increment()
        self.view.set_count(self.model.count)

    def reset_count(self) -> None:
        self.model.reset_count()
        self.view.set_count(self.model.count)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = CounterModel()
    view = CounterView()
    controller = CounterController(model, view)
    view.show()
    app.exec()
