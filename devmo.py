"""
This module provides a demonstration of a simple function.
"""

def function():
    """
    Calculates the sum of two numbers and returns the result.

    Returns:
        int: The sum of 1 and 3.
    """
    a = 1
    b = 3
    c = a + b
    return c

def main():
    """
    Main entry point of the script.
    """
    calculation_result = function()
    print(calculation_result)

if __name__ == "__main__":
    main()
