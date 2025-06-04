# -*- coding: utf-8 -*-

import re
from typing import Final

from .calculator_model import (
    Calculator,
    Expression,
    VALID_CHARACTERS,
)
from .calculator_view import (
    CalculatorWindow,
    CalculatorButton,
)


class CalculatorController:
    def __init__(self, calculator: Calculator, window: CalculatorWindow):
        self.calculator: Final[Calculator] = calculator
        self.window = window

        for button in self.window.buttons.values():
            button.clicked.connect(lambda _, b=button: self.handle_button_click(b))

        # 初期状態のディスプレイを設定
        self.update_display("0")

    def handle_button_click(self, button: CalculatorButton) -> None:
        """ボタン処理"""
        match button.text():
            # リセットボタン
            case "C":
                self.calculator.reset()
                self.update_display("0")
            # イコールボタン
            case "=":
                self.equal_button_clicked()
            # その他のボタン
            case _:
                self.append_expression(button.text())

    def equal_button_clicked(self) -> None:
        """イコールボタン処理"""
        try:
            result = self.calculator.result()
            self.update_display(result)
        except Exception:
            self.update_display("Error")
            self.calculator.expression = Expression()  # 数式をリセット

    def append_expression(self, char: str) -> None:
        """数式に文字を追加する処理"""
        # 現在の数式を取得
        current_expr = self.calculator.expression

        # 新しい文字を検証して追加
        new_expr = InputValidator.validated_expression(current_expr, char)

        # 数式を更新
        self.calculator.expression = new_expr

        self.update_display(self.calculator.expression)

    def update_display(self, value: float | str | Expression) -> None:
        """ディスプレイを更新する"""
        value = str(value) or "0"
        if value.endswith(".0"):
            value = value[:-2]
        self.window.display.setText(value)


class InputValidator:
    """入力の検証を行うクラス"""

    @staticmethod
    def is_valid_expression(input_str: str) -> bool:
        """入力が有効な文字列かどうかをチェック"""
        return all(char in VALID_CHARACTERS for char in input_str)

    @staticmethod
    def validated_expression(
        current_expr: Expression | str, new_char: str
    ) -> Expression:
        """数式の入力を検証した `Expression` を返す"""

        if isinstance(current_expr, Expression):
            current_expr = current_expr.expression

        if not InputValidator.is_valid_expression(new_char):
            raise ValueError(f"Invalid character: {new_char}")

        if len(new_char) != 1:
            raise ValueError("New character must be a single character.")

        # 何も入力されていない場合は current_expr をそのまま返す
        if new_char == "":
            return Expression(current_expr)

        last_char = InputValidator.get_last_char(current_expr)  # 最後の文字を取得
        last_number = InputValidator.get_last_digit(current_expr)  # 最後の数値を取得

        # 正負記号が連続する場合は上書き
        if last_char in "+-" and new_char in "+-":
            return Expression(current_expr[:-1] + new_char)
        # 乗除記号が連続する場合は無視
        if last_char in "*/" and new_char in "*/":
            return Expression(current_expr)
        # 正負記号の次に乗除記号が連続する場合は無視
        if last_char in "+-" and new_char in "*/":
            return Expression(current_expr)

        # 小数点の入力
        if new_char == ".":
            # 数式が空の場合は小数点を0.に変換
            if last_char == "":
                return Expression("0.")
            # 直前の文字が演算子の場合は小数点を0.に変換
            if last_char in "+-*/":
                return Expression(current_expr + "0.")
            # 小数点が連続する場合は無視
            if last_char == ".":
                return Expression(current_expr)
            # 直前の数値に小数点が含まれる場合は無視
            if last_number and "." in last_number:
                return Expression(current_expr)

        # 通常は追加
        return Expression(current_expr + new_char)

    @staticmethod
    def get_last_char(expression: str) -> str:
        """数式の最後の文字を取得"""
        return expression[-1] if expression else ""

    @staticmethod
    def get_last_digit(expression: str) -> str:
        """数式の最後の数値を取得"""
        if expression == "":
            return ""
        return re.split(r"[+\-*/]", expression)[-1]
