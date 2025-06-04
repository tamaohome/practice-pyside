# -*- coding: utf-8 -*-

import pytest

from src.calculator.calculator_model import Calculator


def test_calculator_initialization():
    """初期化"""
    calculator = Calculator()
    assert calculator.expression.expression == ""
    assert calculator.result() == 0.0
    assert calculator.last_result == 0.0


def test_calculator_continuous_calculation():
    """連続計算"""
    calculator = Calculator()
    calculator.expression += "1+2"
    assert calculator.result() == 3.0
    assert calculator.last_result == 3.0

    calculator.expression += "*4"
    assert calculator.result() == 12.0
    assert calculator.last_result == 12.0


def test_calculator_reset():
    """リセット"""
    calculator = Calculator()
    calculator.expression += "1+2"
    assert calculator.expression == "1+2"
    calculator.reset()
    assert calculator.expression == ""
    assert calculator.result() == 0.0
    assert calculator.last_result == 0.0


@pytest.mark.parametrize(
    "expression, expected_result",
    [
        ("1+2*3-4/8", 6.5),
        ("2+3*-4", -10),
        ("-10./-4+8.02", 10.52),
    ],
)
def test_calculator_result(expression, expected_result):
    """計算結果"""
    calculator = Calculator()
    calculator.expression += expression
    assert calculator.result() == expected_result
    assert calculator.last_result == expected_result
