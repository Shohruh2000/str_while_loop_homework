

def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = int(s)
    k = 0
    while x != 0:
        y = x%10

        if y%2==0:
            k +=1
        x //=10
    return k
print(main("12345688"))
    