def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    x1 = 0
    x2 = 0
    while x1<len(s):
        if s[x1].isalpha() and (s[x1]== "a" or s[x1]=="e" or s[x1]=="i" or s[x1]=="o" or s[x1]=="u"):
            x2 +=0
        else:
            x2 +=1
        x1 +=1
    return x2
print(main("assalomualaykum"))