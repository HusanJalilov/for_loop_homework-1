def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s=''
    for i in range(n):
        s+=str(i)+','


    return s[:-1]
print(main(4))