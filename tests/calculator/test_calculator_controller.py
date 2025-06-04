# -*- encoding: utf-8 -*-

import pytest
from PySide6.QtWidgets import QApplication

from src.calculator.calculator_controller import CalculatorController
from src.calculator.calculator_model import Calculator, Expression
from src.calculator.calculator_view import CalculatorWindow, CalculatorButton
from unittest.mock import MagicMock


@pytest.fixture(scope="session", autouse=True)
def app():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app


@pytest.fixture
def calculator():
    """Calculatorのインスタンスを返すフィクスチャ"""
    return Calculator()


@pytest.fixture
def window():
    """CalculatorWindowのインスタンスを返すフィクスチャ"""
    return CalculatorWindow()


@pytest.fixture
def controller(calculator, window):
    """CalculatorControllerのインスタンスを返すフィクスチャ"""
    return CalculatorController(calculator, window)


def test_initial_state(controller, calculator, window):
    """初期状態のテスト"""
    click_buttons(calculator, window, "")

    # ボタンが存在することを確認
    assert len(window.buttons) > 0

    assert window.display.text() == "0"
    assert calculator.expression == ""


def test_continuous_calculation(controller, calculator, window):
    """連続計算のテスト"""
    click_buttons(calculator, window, "1+2")
    assert calculator.expression == "1+2"
    assert window.display.text() == "1+2"

    click_buttons(calculator, window, "=")
    assert calculator.expression == "3.0"
    assert window.display.text() == "3"

    click_buttons(calculator, window, "*4=")
    assert calculator.expression == "12.0"
    assert window.display.text() == "12"


def test_button_click_reset(controller, calculator, window):
    """リセットボタンのクリック"""
    click_buttons(calculator, window, "1+2")

    click_buttons(calculator, window, "C")

    assert calculator.expression == ""
    assert window.display.text() == "0"

    # リセット後に無効な数式を入力しても、表示が0になることを確認
    click_buttons(calculator, window, "/")

    assert calculator.expression == ""
    assert window.display.text() == "0"


def test_button_click_equals(controller, calculator, window):
    """イコールボタンのクリック"""
    click_buttons(calculator, window, "1+2*3")
    assert window.display.text() == "1+2*3"
    assert calculator.expression == "1+2*3"

    click_buttons(calculator, window, "=")
    assert window.display.text() == "7"
    assert calculator.expression == "7.0"


def test_button_click(controller, calculator, window):
    """有効なボタンのクリック"""
    click_buttons(calculator, window, "5+.")

    assert calculator.expression == "5+0."
    assert window.display.text() == "5+0."


def test_button_click_invalid_expression(controller, calculator, window):
    """無効な数式の入力"""
    click_buttons(calculator, window, "1+2*3/")

    # イコールボタンをクリック
    click_buttons(calculator, window, "=")

    # エラーメッセージを確認
    assert window.display.text() == "Error"
    assert calculator.expression == ""


@pytest.mark.parametrize(
    "input_expr,expected_expr",
    [
        ("852.3-*", "852.3-"),
        ("1++..", "1+0."),
        ("5..2", "5.2"),
        ("*.123", "0.123"),
        ("1.2*9..8.", "1.2*9.8"),
    ],
)
def test_button_click_invalid_symbol(
    controller, calculator, window, input_expr, expected_expr
):
    """無効な演算子や記号の入力"""
    click_buttons(calculator, window, input_expr)
    assert calculator.expression == expected_expr


def click_buttons(calculator: Calculator, window: CalculatorWindow, buttons: str):
    """数式を入力するヘルパー関数"""
    for char in buttons:
        button = window.buttons.get(char)
        if button:
            button.click()
        else:
            raise ValueError(f"Button for '{char}' not found in window buttons.")
    return calculator.expression
