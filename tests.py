import pytest
from Calculator import Calculator

class TestCalculator:
    @staticmethod
    def create_calculator():
        """Utility method to create a new instance of the Calculator."""
        return Calculator()

    def test_add(self):
        calc = self.create_calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, -1) == -2

    def test_subtract(self):
        calc = self.create_calculator()
        assert calc.subtract(10, 5) == 5
        assert calc.subtract(-1, -1) == 0

    def test_multiply(self):
        calc = self.create_calculator()
        assert calc.multiply(3, 7) == 21
        assert calc.multiply(-1, -1) == 1

    def test_divide(self):
        calc = self.create_calculator()
        assert calc.divide(10, 2) == 5
        assert calc.divide(-1, -1) == 1
        with pytest.raises(ValueError):
            calc.divide(10, 0)