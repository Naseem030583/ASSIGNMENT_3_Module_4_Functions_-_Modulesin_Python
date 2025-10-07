def factorial(n):
    """ Calculate factorial of a number using recursion.
    Args:
        n: A non-negative integer
    Returns:
        The factorial of n
    """
    if n == 0 :
        return 1
    return n * factorial(n - 1)
number = int(input("Enter a number: "))
result = factorial(number)
print(f"Factorial of {number} is: {result}")
