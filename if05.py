def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    n=n//10
    x2=n%10
    n=n//10
    x3=n%10
    n=n//10
    x4=n%10
    n=n//10
    x5=n%10

    if x1>x2:
        if x1>x3:
            if x1>x4:
                if x1>x5:
                    answer=x1
    elif x2>x1:
        if x2>x3:
            if x2>x4:
                if x2>x5:
                    answer=x2
    elif x3>x1:
        if x3>x2:
            if x3>x4:
                if x3>x5:
                    answer=x3
    elif x4>x1:
        if x4>x2:
            if x4>x3:
                if x4>x5:
                    answer=x4
        else:
            answer=x5
    return  answer
print(main(23546))