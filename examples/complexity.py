# given a function, what is its time complexity?
from algoaid import analyse
import math


# A function
def f(n):
    i = 1
    while i < n:
        i += math.isqrt(i)
        for j in range(1, n//10):
            for k in range(math.isqrt(n)):
                i % j == k


if __name__ == '__main__':
    analyse(f, nmax=5000)
