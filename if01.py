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
    if a>b>c:
        answer=a
    elif a<b<c:
        answer=c
    elif a<b>c:
        answer=b
    
    return answer
print(main(1,4,2))