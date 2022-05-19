from collections import deque
from random import choice, choices, shuffle, sample
deque


# sample => original remains unchanged, shuffle => shuffles the original... /// Organiza a lista
class Objeto:
    def __init__(self, title, num_max):
        self.range_sorteio = range(1, num_max+1)

    def cria_sorteio(self, qtd_nums: int, sorted=True):
        range_sorteio = self.range_sorteio or range(1, 60+1)
        list_nums = list(range_sorteio)
        tam_jogada = qtd_nums
        jogada = []
        for i in range(tam_jogada):
            num = choice(list_nums)
            while num in jogada:
                num = choice(list_nums)
            jogada.append(num)
        if sorted:
            jogada.sort()
        return jogada


megasena = Objeto("MEGA-SENA", 60)

lotofacil = Objeto("LOTOFACIL", 25)

a = megasena.cria_sorteio(6)
print(a)

a = lotofacil.cria_sorteio(15)
print(a)
