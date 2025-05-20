# -*- coding: utf-8 -*-

from PySide6.QtWidgets import (
    QMainWindow,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .tree_model import TreeNode


class TreeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree Viewer")
        self.resize(320, 320)
        main_widget = QWidget()
        self.v_layout = QVBoxLayout(main_widget)
        self.tree = NodeTreeWidget()
        self.v_layout.addWidget(self.tree)
        self.setCentralWidget(main_widget)


class NodeTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIndentation(10)
        self.setHeaderLabels(["Level", "Name"])

    def set_tree(self, root_node: TreeNode) -> None:
        self.clear()

        def add_items(parent_item, node):
            item = QTreeWidgetItem(parent_item, [node.level, node.name])
            for child in node.children:
                add_items(item, child)

        add_items(self, root_node)
        self.expandAll()
