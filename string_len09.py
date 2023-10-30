def main(n1, n2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    s1=int(n1)
    s2=int(n2)
    d=str(s1+s2)
    return ('"'+d+'"')
n1=12
n2=7
print(main(n1,n2))