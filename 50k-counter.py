import os
import timeit
os.system("color 2")
timerstart = timeit.default_timer()
a = 0
while a <= 50000:
    a += 1
    print(a)
timerstop = timeit.default_timer()
timerresult = timerstop - timerstart
print("time result: ", "%.2f" % timerresult, "seconds")
input()