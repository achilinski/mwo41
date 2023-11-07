class Calculator:
    """A simple calculator class."""

    def add(self, x, y):
        """Return the sum of x and y."""
        return x + y

    def subtract(self, x, y):
        """Return the subtraction of y from x."""
        return x - y

    def multiply(self, x, y):
        """Return the product of x and y."""
        return x * y

    def divide(self, x, y):
        """Return the division of x by y."""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y