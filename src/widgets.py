# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QCheckBox,
    QRadioButton,
    QComboBox,
    QSpinBox,
    QSlider,
    QProgressBar,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QGroupBox,
)
from PySide6.QtCore import Qt
from .flowlayout import FlowLayout


class WidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Showcase")
        self.setMinimumSize(500, 0)

        main_layout = QFormLayout()
        main_layout.setVerticalSpacing(20)
        main_layout.setHorizontalSpacing(20)

        # ラベル
        main_layout.addRow("ラベル (QLabel)", QLabel("ラベル表示のサンプル"))

        # ボタン
        main_layout.addRow("ボタン (QPushButton)", QPushButton("ボタン"))

        # テキスト入力
        main_layout.addRow("テキスト入力 (QLineEdit)", QLineEdit("初期値"))

        # テキストエリア
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("ここに自由に入力")
        text_edit.setFixedHeight(60)
        main_layout.addRow("複数行テキスト (QTextEdit)", text_edit)

        # チェックボックス
        checkbox_labels = ["氷", "ミルク", "砂糖"]
        checkbox_buttons = [QCheckBox(label) for label in checkbox_labels]
        checkbox_buttons[0].setChecked(True)  # 氷を初期選択

        checkbox_layout = FlowLayout()
        [checkbox_layout.addWidget(checkbox) for checkbox in checkbox_buttons]
        main_layout.addRow("チェックボックス (QCheckBox)", checkbox_layout)

        # ラジオボタン
        radio_labels = ["Sサイズ", "Mサイズ", "Lサイズ"]
        radio_buttons = [QRadioButton(label) for label in radio_labels]
        radio_buttons[1].setChecked(True)  # 普通盛りを初期選択

        radio_layout = FlowLayout()
        [radio_layout.addWidget(radio) for radio in radio_buttons]
        radio_group = QGroupBox()
        radio_group.setStyleSheet("QGroupBox { border: none; }")
        radio_group.setLayout(radio_layout)
        main_layout.addRow("ラジオボタン (QRadioButton)", radio_group)

        # コンボボックス（ドロップダウン）
        combo = QComboBox()
        combo.addItems(["コーヒー", "紅茶", "炭酸水", "ミネラルウォーター"])
        main_layout.addRow("選択リスト (QComboBox)", combo)

        # 数値入力（スピンボックス）
        spin = QSpinBox()
        spin.setRange(0, 10)
        spin.setValue(1)
        main_layout.addRow("数値入力 (QSpinBox)", spin)

        # スライダー
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 10)
        slider.setValue(5)
        slider.setSingleStep(1)
        main_layout.addRow("スライダー (QSlider)", slider)

        # プログレスバー
        progress = QProgressBar()
        progress.setValue(90)
        main_layout.addRow("プログレスバー (QProgressBar)", progress)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WidgetExample()
    window.show()
    sys.exit(app.exec())
