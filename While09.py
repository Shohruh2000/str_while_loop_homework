


def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    
    x = int(s)
    k = 0
    while x != 0:
        y = x%10

        if y !=0:
            k +=y

        x //=10
    return k

print(main("1052")) 
