import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 8) == 16

    def test_division_success(self):
        assert self.calc.division(9, 3) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(35, 7) == 28

    def test_adding_success(self):
        assert self.calc.adding(2, 5) == 7

    def teardown(self):
        print("Выполнение метода Teardown")

