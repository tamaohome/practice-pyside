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
        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Middle"))
        layout.addWidget(QPushButton("Bottom"))
        group.setLayout(layout)
        return group

    def _create_hbox_group(self) -> QGroupBox:
        """横並びレイアウト"""
        group = QGroupBox("QHBoxLayout")
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Left"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Right"))
        group.setLayout(layout)
        return group

    def _create_grid_group(self) -> QGroupBox:
        """グリッドレイアウト"""
        group = QGroupBox("QGridLayout")
        layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                num = i * 3 + j + 1
                layout.addWidget(QPushButton(f"No.{num}"), i, j)
        group.setLayout(layout)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LayoutsExample()
    window.show()
    sys.exit(app.exec())
