from prime_nums import is_prime, get_prime_nums
import numpy
# check if is num_primo

# def __next_prime():


def mult(*nums): return numpy.prod(nums)


def merge(a, b):
    from collections import Counter
    na, nb = Counter(a), Counter(b)
    return list(Counter({k: max((na[k], nb[k])) for k in set(a + b)}).elements())


def get_mmc(*nums):

    # 1 é divisível somente por ele mesmo, por isso não é primo
    max_primes = max(nums)

    primes = get_prime_nums(99, max_num=max_primes)

    pris_full_list = []
    # pri de primes

    for n in nums:
        pris_list = []
        print(n)
        calc_n = n
        while calc_n != 1:
            for pri in primes:
                if calc_n % pri == 0:
                    calc_n /= pri
                    # print(calc_n, ', ', end='')
                    pris_list.append(pri)
                    print(pri, ' n: ', calc_n)
        pris_full_list.append(pris_list)
    print(pris_full_list)
    # MAKE THE MERGE
    # final_pris_full = []
    for cont, lispri in enumerate(pris_full_list[1:]):
        if cont == 0:
            # mergir a 0º com 1º
            final_pris_full = merge(pris_full_list[cont], lispri)
        else:
            final_pris_full = merge(final_pris_full, lispri)

    print('~'*30)
    print(f'MMC de {nums} é {mult(final_pris_full)}')
    print('~'*30)
    # FUNCIONANDO!!!!!
    # input(final_pris_full)


print(f'{"Mínimo Múltiplo Comum (MMC)":~^60}')
print('{:^60}'.format("Separe os parâmetros por ,"))

user_nums = eval(input('Digite os N: '))
the_mmc = get_mmc(
    *user_nums) if hasattr(user_nums, '__iter__') else get_mmc(user_nums)

# print(the_mmc)
