def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>c:
        if b>c:
            answer=c
    elif a<b:
        if a<c:
            answer=a
    elif a>b:
        if c>b:
            answer=b
    return answer
print(main(-5,-3,-1))