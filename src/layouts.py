# -*- coding: utf-8 -*-

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFormLayout,
    QPushButton,
    QLineEdit,
    QGroupBox,
    QSizePolicy,
)
import sys


class LayoutsExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts Example")
        self.setMinimumSize(400, 500)

        main_layout = QVBoxLayout()

        # 各レイアウトのグループを作成
        main_layout.addWidget(self._create_vbox_group())
        main_layout.addWidget(self._create_hbox_group())
        main_layout.addWidget(self._create_grid_group())
        main_layout.addWidget(self._create_form_group())

        self.setLayout(main_layout)

    def _create_vbox_group(self) -> QGroupBox:
        """縦並びレイアウト"""
        group = QGroupBox("QVBoxLayout")
        layout = QVBoxLayout()
        layout.addWidget(MyButton("Top"))
        layout.addWidget(MyButton("Middle"))
        layout.addWidget(MyButton("Bottom"))
        group.setLayout(layout)
        return group

    def _create_hbox_group(self) -> QGroupBox:
        """横並びレイアウト"""
        group = QGroupBox("QHBoxLayout")
        layout = QHBoxLayout()
        layout.addWidget(MyButton("Left"))
        layout.addWidget(MyButton("Center"))
        layout.addWidget(MyButton("Right"))
        group.setLayout(layout)
        return group

    def _create_grid_group(self) -> QGroupBox:
        """グリッドレイアウト"""
        group = QGroupBox("QGridLayout")
        layout = QGridLayout()
        for row in range(3):
            for col in range(5):
                label = f"Cell {row + 1}-{col + 1}"
                layout.addWidget(MyButton(label), row, col)
        group.setLayout(layout)

        # セルのマージ
        # INFO: 以下の処理では指定のセルに上書きする形でセル結合を行っている。
        #       ただし、既存のアイテムは削除されずにフォーカス可能な状態として残る。
        #       そのため、実際のコードでは、結合されるセルを空にする必要がある。
        layout.addWidget(MyButton("Merged Cell"), 0, 0, 2, 2)
        layout.addWidget(MyButton("Horizontally Merged Cell"), 2, 0, 1, 3)
        layout.addWidget(MyButton("Vertically\nMerged\nCell"), 1, 4, 2, 1)

        return group

    def _create_form_group(self) -> QGroupBox:
        """フォームレイアウト"""
        group = QGroupBox("QFormLayout")
        layout = QFormLayout()
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Email:", QLineEdit())
        layout.addRow("Password:", QLineEdit())

        btn_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        submit_btn.setFixedWidth(80)
        reset_btn = QPushButton("Reset")
        reset_btn.setFixedWidth(80)
        btn_layout.addWidget(submit_btn)
        btn_layout.addWidget(reset_btn)
        layout.addRow("", btn_layout)
        group.setLayout(layout)
        return group


class MyButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(50, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LayoutsExample()
    window.show()
    sys.exit(app.exec())
