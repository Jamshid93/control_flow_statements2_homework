def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b:
        if a>c:
            answer=a
    elif a<b:
        if b>c:
            answer=b
        else:
            answer=c
    return answer

print(main(-5,-3,-1))