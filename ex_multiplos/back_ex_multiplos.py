from prime_nums import is_prime, get_prime_nums
import numpy
# check if is num_primo

# def __next_prime():


def mult(*nums): return numpy.prod(nums)


def get_mmc(*nums):

    # 1 é divisível somente por ele mesmo, por isso não é primo
    max_primes = max(nums)

    __primos = get_prime_nums(99, max_num=max_primes)

    nums_e_divs = {}
    for n in nums:
        calc_n = n
        nums_e_divs[n] = []
        while calc_n != 1:
            for mmc_div in __primos:
                while calc_n % mmc_div == 0:
                    calc_n //= mmc_div
                    nums_e_divs[n].append(mmc_div)
                    # print(calc_n)
    # input(f'n divisors: {n_divisors}')

    def printer():
        print('~' * 30)

        # a key com mais valores inseridos
        # qtd_linhas = int(max(str(len(nums_e_divs.values()))))
        def get_qtd_linhas():
            qtd_linhas = []
            for vv in nums_e_divs.values():
                if len(vv) > len(qtd_linhas):
                    qtd_linhas = vv
            return len(qtd_linhas)
        qtd_linhas = get_qtd_linhas()
        # ------------ Create lista_divisors
        _lista__divisors = []
        for __i in range(qtd_linhas):
            # ndv = n_divisors
            ndv_vals = [v for v in nums_e_divs.values()]
            in_lista_div = []
            for divisors in ndv_vals:
                try:
                    in_lista_div.append(divisors[__i])
                except IndexError:
                    pass
            _lista__divisors.append(in_lista_div)
        # ------------ Create lista_divisors

        # ------------ Create PRINT
        nums2calc = list(nums_e_divs.keys())
        __ = nums_e_divs.keys()

        dinamic_mmc_counter = 0

        _multsets = []

        for __i in range(qtd_linhas):
            _lsdiv_set = set()
            _lsdiv = _lista__divisors[__i]

            for epk, val in enumerate(nums2calc):
                print(val, end=', ' if epk != len(
                    nums_e_divs) - 1 else ' | ')

                if val != 1:
                    try:
                        nums2calc[epk] //= _lsdiv[dinamic_mmc_counter]
                    except IndexError:
                        pass
                    dinamic_mmc_counter += 1

            for ed, div in enumerate(_lsdiv):
                if ed == len(_lsdiv) - 1:

                    print(div, end='')
                else:
                    print(div, end=', ')
                _lsdiv_set.add(div)
            print()
            _multsets.append(list(_lsdiv_set))

        # ------------------ cria resultado
        mult_lists = []
        for vs in _multsets:
            if isinstance(vs, list):
                mult_lists += [v for v in vs]
            else:
                mult_lists.append(vs)

        input(mult_lists)
        print('1, 1')

        print('~' * 30)

        print('O resultado é: ', mult(*mult_lists))
        print('~' * 30)

        # ------------ Create PRINT
        # for val in n_divisors.values():
        #     print(val)
    printer()


print(f'{"Mínimo Múltiplo Comum (MMC)":~^60}')
print('{:^60}'.format("Separe os parâmetros por ,"))

user_nums = eval(input('Digite os N: '))


the_mmc = get_mmc(
    *user_nums) if hasattr(user_nums, '__iter__') else get_mmc(user_nums)

# print(the_mmc)


# taaaaaaa erraaaaaadooooooooooooooooooo
#  somente um N aparece por tabela
