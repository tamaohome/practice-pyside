# -*- coding: utf-8 -*-

import pytest

from src.calculator.calculator_model import Expression


@pytest.mark.parametrize(
    "input_expr, expected_result",
    [
        ("1+2*3-4/8", 6.5),
        ("2+3*4", 14),
        ("10/-4+8", 5.5),
        ("7-3*2", 1),
        ("8/4+2*3", 8),
    ],
)
def test_expression(input_expr, expected_result):
    """有効な数式の入力"""
    expr = Expression(input_expr)
    assert expr.expression == input_expr
    assert expr.result == expected_result


@pytest.mark.parametrize(
    "invalid_expr",
    [
        "1+2*3-4/8P",
        "2+2a",
        "5/0x",
        "abc",
        "1+2*3-4/8!",
    ],
)
def test_expression_with_invalid_chars(invalid_expr):
    """無効な文字を含む入力"""
    with pytest.raises(ValueError):
        Expression(invalid_expr)


@pytest.mark.parametrize(
    "valid_expr, expected_result",
    [
        ("2*+3", 6),
        ("3*-4", -12),
        ("-10/+2", -5),
        ("10/-4", -2.5),
    ],
)
def test_expression_with_valid_duplicate_operators(valid_expr, expected_result):
    """有効な演算子の重複を含む入力"""
    expr = Expression(valid_expr)
    assert expr.expression == valid_expr
    assert expr.result == expected_result


@pytest.mark.parametrize(
    "invalid_expr",
    [
        "1++2",
        "3---4",
        "5**2",
        "6//3",
        "7+-8",
        "9*/2",
        "10//+5",
    ],
)
def test_expression_with_invalid_duplicate_operators(invalid_expr):
    """無効な演算子の重複を含む入力"""
    with pytest.raises(ValueError):
        Expression(invalid_expr)


def test_expression_with_zero_division():
    """ゼロ除算エラーの発生"""
    with pytest.raises(ZeroDivisionError):
        Expression("5/0").result
