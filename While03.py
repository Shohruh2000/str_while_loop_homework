def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0
    j = 0
    while i < len(s):
        if s[i].isdigit():
            k +=1
        elif s[i].isalpha():
            j +=1
        i = i+1
        
    return (len(s)-k-j)
print(main("12@#sd*12"))