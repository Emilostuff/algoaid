from algoaid import analyse


def f(n):
    j = 1
    while j * j < n:
        j += 1


if __name__ == '__main__':
    analyse(f)
