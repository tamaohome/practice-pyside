# -*- coding: utf-8 -*-

from PySide6.QtWidgets import (
    QMainWindow,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt

from .tree_model import TreeNode


class TreeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree Viewer")
        self.resize(400, 300)
        main_widget = QWidget()
        self.v_layout = QVBoxLayout(main_widget)
        self.tree = NodeTreeWidget()
        self.v_layout.addWidget(self.tree)
        self.setCentralWidget(main_widget)


class NodeTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIndentation(10)
        self.setHeaderLabels(["Level", "Name", "Items"])
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 200)
        self.setColumnWidth(2, 0)

    def set_tree(self, root_node: TreeNode) -> None:
        self.clear()

        def add_items(parent_item, node):
            leaves_count = str(len(node.children))
            item = QTreeWidgetItem(parent_item, [node[0], node[1], leaves_count])
            item.setTextAlignment(2, Qt.AlignmentFlag.AlignRight)
            for child in node.children:
                add_items(item, child)

        add_items(self, root_node)
        self.expandAll()
