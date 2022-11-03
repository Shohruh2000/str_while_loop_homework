def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = int(s)
    k = 0
    while x != 0:
        y = x%10

        if y%2==1:
            k +=y
        x //=10
    return k
print(main("12345"))