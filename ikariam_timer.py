from win10toast import ToastNotifier
from time import sleep
from sys import argv

min = float(argv[1])


def min2sec(x: float): return int(x * 60)


tosleep_min = min2sec(min)
try:
    tosleep_secs = argv[2]
    tosleep = tosleep_min + tosleep_secs
except IndexError:
    tosleep = tosleep_min

for i in range(tosleep):
    sleep(1)
    print(i)


toaster = ToastNotifier()
toaster.show_toast(
    "TOMAR REMÉDIO", duration=1)
