def recursividade_elevado(n):
    return n * n


def mult(m, n):
    print(n)
    if n > 1:
        return m * n
    else:
        mult(m, n-1) + m
    # return n if n == 1 else n*factorial(n-1)


print(mult(3, 10))
