from prime_nums import get_prime_nums, is_prime
from numpy import prod


def get_mdc(*nums):
    def same_divisor(prmn) -> bool:
        # prmn = prime_num
        if not is_prime(prmn):
            # prmn = get_prime_nums(1, prmn)[0]
            # raise ValueError(f"\033[1;31mint({prmn}) não é primo \033[m")
            pass
        for n in nums:
            if not n % prmn == 0:
                break
        else:
            yield prmn
    resp = [r for _val in range(2, int(max(nums)/2))
            for r in same_divisor(_val)]
    # mults = map(is_prime, resp)
    mults = filter(is_prime, resp)
    mults = list(mults)
    # MAP retorna o valor literal que a função a mapear retorna
    # FILTER retorna os valores do array se True
    return prod(mults)


a = get_mdc(44, 88, 264)
print(a)
