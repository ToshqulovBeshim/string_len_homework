def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    return s2 if len(s1)>len(s2) else s1
s1="2223rfgvdsdf"
s2="fgh"
print(main(s1,s2))