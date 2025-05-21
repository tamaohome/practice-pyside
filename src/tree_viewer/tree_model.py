# -* coding: utf-8 -*-

from anytree import NodeMixin
from pathlib import Path
import csv
from typing import Final


class TreeNode(NodeMixin):
    def __init__(self, row: list[str]):
        if len(row) < 2:
            row = ["", ""]
        self.row: Final[list[str]] = row
        self.level: Final[int] = int(row[0].strip("#"))
        self.name: Final[str] = row[1].strip()
        self.parent: TreeNode | None
        self.children: list[TreeNode] = []

    def __repr__(self):
        return f"TreeNode({self.name})"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return self.level == other.level and self.name == other.name

    def __getitem__(self, index: int) -> str:
        if 0 <= index < len(self.row):
            return self.row[index]
        else:
            raise IndexError("Index out of range")

    def find_child(self, name: str) -> "TreeNode | None":
        for child in self.children:
            if child.name == name.strip():
                return child
        return None


class TreeNodeBuilder:
    def __init__(self, csv_path: Path):
        self.root = TreeNode(["0", "root"])
        self.nodes: dict[int, list[TreeNode]] = {0: [self.root]}
        self._build_from_csv(csv_path)

    def _build_from_csv(self, csv_path: Path) -> None:
        with csv_path.open(encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                self._append_node(row)

    def _append_node(self, row: list[str]) -> None:
        if not row or not row[0].startswith("#"):
            return

        node = TreeNode(row)

        parent = self.nodes[node.level - 1][-1]
        if current_node := parent.find_child(node.name):
            self.nodes[current_node.level].append(current_node)
            return
        node.parent = parent
        self.nodes.setdefault(node.level, []).append(node)

    def find_node(self, level: int, name: str) -> TreeNode | None:
        for node in self.nodes.get(level, []):
            if node.name == name:
                return node
        return None
