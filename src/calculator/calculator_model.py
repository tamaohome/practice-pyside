# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass

SYMBOLS = set("+-*/=")
DIGITS = set("0123456789.")
BRACKETS = set("()")
VALID_CHARACTERS = DIGITS | SYMBOLS | BRACKETS


class Calculator:
    """電卓の状態を保持するクラス"""

    def __init__(self):
        self._expression = Expression()
        self._result_history: list[float] = []

    def reset(self) -> None:
        """電卓の状態をリセット"""
        self._expression = Expression()

    def result(self) -> float:
        """数式の計算結果を返す"""
        result = self._expression.result
        self._result_history.append(result)
        self._expression = Expression(result)  # 数式をリセット
        return result

    @property
    def last_result(self) -> float:
        """最後の計算結果を返す"""
        if not self._result_history:
            return 0.0
        return self._result_history[-1]

    @property
    def expression(self) -> "Expression":
        """現在の数式を返す"""
        return self._expression

    @expression.setter
    def expression(self, value: "Expression") -> None:
        """数式を設定"""
        if not isinstance(value, Expression):
            raise TypeError("Expression must be an instance of Expression class")
        self._expression = value


@dataclass(frozen=True)
class Expression:
    """数式を保持するデータクラス"""

    expression: str = ""

    def __init__(self, expression: str | float = ""):
        expression = str(expression)
        if not self._is_valid_expression(expression):
            raise ValueError(f"Invalid expression: {expression}")
        object.__setattr__(self, "expression", expression)

    def __str__(self) -> str:
        return self.expression

    def __repr__(self) -> str:
        return f"Expression({self.expression!r})"

    def __eq__(self, other: object) -> bool:
        """数式の等価性を比較"""
        if isinstance(other, Expression):
            return self.expression == other.expression
        if isinstance(other, str):
            return self.expression == other
        return NotImplemented

    def __add__(self, char: str) -> "Expression":
        """数式に文字を追加"""
        if not isinstance(char, str):
            raise TypeError("Only string can be added to Expression")
        return Expression(self.expression + char)

    def _is_valid_expression(self, expression: str) -> bool:
        """数式の有効性をチェック"""
        # 空の数式は許可する
        if len(expression) == 0:
            return True
        # 有効な文字以外は許可しない
        if any(char not in VALID_CHARACTERS for char in expression):
            return False
        # 先頭の乗除記号は許可しない
        if expression[0] in "*/":
            return False
        # 連続するドットを許可しない
        if re.search(r"\.\.+", expression):
            return False
        # 連続する演算子を許可しない
        # 許可する並び: "*+", "*+", "/+", "/-"
        if (
            re.search(r"[+\-][+\-]", expression)
            or re.search(r"[*/][*/]", expression)
            or re.search(r"[+\-][*/]", expression)
        ):
            return False

        return True

    def _evaluate(self) -> float:
        """数式を評価して結果を返す"""
        if self.expression == "":
            return 0.0
        try:
            return float(eval(self.expression, {"__builtins__": None}, {}))
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero in expression: {self.expression}")
        except SyntaxError:
            raise SyntaxError(f"Invalid syntax in expression: {self.expression}")
        except Exception as e:
            raise ValueError(f"Invalid expression: {self.expression}") from e

    @property
    def result(self) -> float:
        """数式の評価結果を返す"""
        return self._evaluate()
