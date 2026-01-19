import math


def add(a, b):
    """Add two numbers."""
    return a + b


def square(x):
    """Return square of a number."""
    return x * x


def calculate_area(radius):
    """
    Calculate area of a circle.
    Uses math.pi and square().
    """
    r_squared = square(radius)
    return math.pi * r_squared


def main():
    r = 5
    area = calculate_area(r)
    print("Area:", area)


if __name__ == "__main__":
    main()
