def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>=b and a<=c:
        answer=a
    elif a<=b and b<=c:
        answer=b
    else:
        answer=c
    return answer
print(main(3,7,10))