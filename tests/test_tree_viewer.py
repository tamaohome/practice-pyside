# -*- coding: utf-8 -*-

import pytest
from pathlib import Path
from anytree import RenderTree

from src.tree_viewer.tree_model import TreeNode, TreeNodeBuilder

sample_csv_path = Path("sample_data/fish_list.csv")


def test_tree_node_builder():
    tree_builder = TreeNodeBuilder(sample_csv_path)

    root = tree_builder.root
    assert root is not None
    assert root.depth == 0
    assert root.size == 12

    child = root.children[0].children[0].children[0].children[0]
    assert child is not None
    assert child.depth == 4
    assert len(child.children) == 2
    assert child.size == 8

    # ツリー階層の表示
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.level} {node.name}")
