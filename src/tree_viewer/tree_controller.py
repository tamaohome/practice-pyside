# -*- coding: utf-8 -*-

from pathlib import Path
from .tree_model import TreeNode
from .tree_model import TreeNodeBuilder
from .tree_view import TreeWindow


class TreeController:
    def __init__(self, view: TreeWindow):
        self._view = view
        self._tree_node: TreeNode | None = None

    def set_tree_node(self, csv_path: Path) -> None:
        builder = TreeNodeBuilder(csv_path)
        self._tree_node = builder.root.children[0]
        self._view.tree.set_tree(self._tree_node)
