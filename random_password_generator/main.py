import random
import sys


def getIncludedChars(excluded_chars=''):
    included_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+\\|[{}];:"\',<.>/?`~'
    res = [c for c in included_chars if c not in excluded_chars]
    return ''.join(res)


def getRandomChar(excluded_chars=''):
    included_chars = getIncludedChars(excluded_chars)
    idx = random.randint(0, len(included_chars) - 1)
    return included_chars[idx]


def generateRandomString(n=10, excluded_chars=''):
    res = ''
    for _ in range(n):
        res += getRandomChar(excluded_chars)
    return res


if __name__ == '__main__':
    args = sys.argv
    size = int(args[1]) if len(args) > 1 else 10
    ex_chars = args[2] if len(args) > 2 else ''
    s = generateRandomString(size, ex_chars)
    print(s)
