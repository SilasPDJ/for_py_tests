import subprocess
from sys import argv


def frase(*frases):
    total = []
    for f in frases[-1::-1]:

        total.append("".join([_ for _ in f[-1::-1]]))
        # total.append("".join([_ for _ in f[::2]+f[1::2]]))

    return " ".join(total)


data = txt = frase(*argv[1:])
subprocess.run(['clip.exe'], input=txt.strip().encode(
    'utf-16'), check=True, shell=True)
