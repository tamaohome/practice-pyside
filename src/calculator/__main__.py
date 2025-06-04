# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication
from .calculator_model import Calculator
from .calculator_view import CalculatorWindow
from .calculator_controller import CalculatorController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Calculator()
    window = CalculatorWindow()
    controller = CalculatorController(model, window)
    window.show()

    sys.exit(app.exec())
