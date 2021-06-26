import sys

steps = sys.argv[1]
steps_int = int(steps)

n = steps_int
k = 1

for i in range(steps_int):
    print(" "*(n - 1) + "#"*k)
    n -= 1
    k += 1