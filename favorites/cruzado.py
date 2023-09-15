import subprocess
from sys import argv


def remove_repeats(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def frase(*frases):
    total = []
    total_back = []
    _frases = " ".join(frases)
    for i in range(len(_frases)):
        will = _frases[:i+1].strip()
        if will not in total:
            total.append(will)

    for i in range(len(_frases) - 1, -1, -1):
        will = _frases[:i].strip()
        if will.strip() not in total_back:
            total_back.append(will)
    total = remove_repeats(total)
    total_back = remove_repeats(total_back)
    total_full = total + total_back

    return "\n".join(total_full)


data = txt = frase(*argv[1:])

subprocess.run(['clip.exe'], input=txt.strip().encode(
    'utf-16'), check=True, shell=True)
