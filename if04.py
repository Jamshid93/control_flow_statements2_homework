def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a>b:
        answer=a
    elif a==b:
        answer=0
    else:
        answer=b
    return answer
print(main(5,5))