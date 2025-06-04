# -*- coding: utf-8 -*-

import pytest

from src.calculator.calculator_model import Calculator
from src.calculator.calculator_controller import InputValidator


@pytest.fixture
def calculator():
    """Calculatorのインスタンスを提供するフィクスチャ"""
    return Calculator()


def test_is_valid_input(calculator):
    """有効な入力の検証"""
    valid_inputs = ["1", "+2.", "+", "2/-4", "5*", "3/+", ".9*-"]
    for input_str in valid_inputs:
        assert InputValidator.is_valid_expression(input_str)


@pytest.mark.parametrize(
    "current_expr, new_char, expected",
    [
        # 正負記号が連続する場合は上書き
        ("1+2*3-", "+", "1+2*3+"),
        ("1+2*3+", "-", "1+2*3-"),
        # 乗除記号が連続する場合は無視
        ("1+2*3/", "*", "1+2*3/"),
        ("1+2*3/", "+", "1+2*3/+"),
        # 小数点が連続する場合は無視
        ("1+2.", ".", "1+2."),
        # 直前の数値に小数点が含まれる場合は無視
        ("1+2.34", ".", "1+2.34"),
        # 自動で0を追加するケース
        ("", ".", "0."),
        ("1+2*", ".", "1+2*0."),
    ],
)
def test_validate_expression(calculator, current_expr, new_char, expected):
    """演算記号の上書き"""
    validated_expr = InputValidator.validated_expression(current_expr, new_char)
    assert validated_expr == expected
