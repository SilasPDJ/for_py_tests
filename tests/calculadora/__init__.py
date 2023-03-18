def soma(x, y):
    """
    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: Variável precisa ser int ou float
    """
    msg = 'Variável precisa ser int ou float'
    assert isinstance(x, (int, float)), msg
    assert isinstance(y, (int, float)), msg
    # Assert geralmente é para outros devs
    return x + y


def subtrai(x, y):
    msg = 'Variável precisa ser int ou float'
    assert isinstance(x, (int, float)), msg
    assert isinstance(y, (int, float)), msg
    return x - y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
