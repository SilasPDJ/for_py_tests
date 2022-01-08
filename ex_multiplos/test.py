lista = [[2, 3, 3], [3, 11], [2, 241]]

lista_vai_ficar = [[2, 3, 2], [3, 11, 241], [3]]

for e in range(3):
    for partes in lista:
        try:
            print(partes[e], end=' ')
        except IndexError:
            pass
    print()

