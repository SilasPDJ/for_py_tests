from prime_nums import get_prime_nums, is_prime


def factorial(n):
    return n if n == 1 else n*factorial(n-1)


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonnaci(qtd: int):
    lista = list()
    return [i if len(lista) <= 1 else lista.append(
        lista[-1]+lista[-2]) for i in range(qtd)]


def fibo_padrao(qtd=20):
    cont = 0
    t1, t2 = 0, 1
    while cont < qtd:
        t3 = t1 + t2
        yield t3
        t1, t2 = t2, t3
        cont += 1
