# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

from .tree_view import TreeWindow
from .tree_controller import TreeController


if __name__ == "__main__":
    csv_path = Path("sample_data/fish_list.csv")

    app = QApplication(sys.argv)
    window = TreeWindow()
    controller = TreeController(window)
    window.show()

    controller.set_tree_node(csv_path)

    sys.exit(app.exec())
