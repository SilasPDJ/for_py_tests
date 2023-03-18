from calculadora import soma

try:
    s = soma(15, '15')

    print(s)
except AssertionError as e:
    print(f'Conta invalida: {e}')
