# -* coding: utf-8 -*-

from anytree import NodeMixin
from pathlib import Path
import csv
from typing import Final


class TreeNode(NodeMixin):
    def __init__(self, level: str, name: str, parent=None):
        self.level: Final[str] = level
        self.name: Final[str] = name
        self.parent: TreeNode | None = parent
        self.children: list[TreeNode] = []

    def __repr__(self):
        return f"TreeNode({self.name})"

    def __str__(self):
        return self.name


class TreeNodeBuilder:
    def __init__(self, csv_path: Path):
        self.nodes: dict[int, TreeNode] = {}
        self.root = self._build_from_csv(csv_path)

    def _build_from_csv(self, csv_path: Path) -> TreeNode:
        with csv_path.open(encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row or not row[0].startswith("#"):
                    continue
                node = TreeNode(*row)
                level = int(row[0][1:])
                name = row[1].strip()

                # 階層および名称が重複している場合はスキップ
                if level in self.nodes and name == self.nodes[level].name:
                    continue

                self.nodes[level] = node
                if level == 1:
                    self.root = node
                else:
                    parent = self.nodes[level - 1]
                    node.parent = parent

        return node.root
