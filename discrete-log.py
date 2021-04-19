from math import ceil
import time


# Finding multiplicative inverse
def multiplicative_inverse(r2, r1=26):
    # Using Extended Euclidean Algorithm with modifications
    m = r1
    t1, t2 = 0, 1
    while True:
        if r2 == 0:
            # Uncomment to see steps
            # print("q = {},r1 ={},r2={}, r ={}, t1={},t2={}, t={}".format('', r1, r2, '', t1, t2, '*'))
            break
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        # Uncomment to see steps
        # print("q = {},r1 ={},r2={}, r ={}, t1={},t2={}, t={}".format(q, r1, r2, r, t1, t2, t))

        r1, r2, t1, t2 = r2, r, t2, t
    gcd = r1
    # print("Gcd is",gcd)
    if gcd != 1:
        return None
    else:
        # print("Inverse is", t1%m)
        return t1 % m


# Naive algorithm for discrete log
def naive_dlp(g, y, p):
    current = 1
    if y == 1:
        return 0
    for i in range(1, p + 1):
        current = current * g % p
        if current == y:
            return i
    return -1


# bsgs algorithm for discrete log
def baby_step_giant_step_dlp(g, y, p):
    m = ceil(p ** (1 / 2))

    # table for storing {g^j : j}
    table = {1: 0}
    current = 1
    if y == 1:
        return 0
    # Computing g^-m mod p
    # Modular exponentiation and Extended Euclidean Algorithm
    # g^m(p-2) mod p can also be used - By Fermat Theorem
    g_minus_m = pow(multiplicative_inverse(g, p), m, p)

    # storing g^j
    for j in range(1, m):
        current = g * current % p
        if current not in table:
            table[current] = j
    # finding collision with y[(g^-m)]^i
    current = 1
    for i in range(1, m):
        current = (g_minus_m * current) % p
        arg = y * current % p
        if arg in table:
            return table[arg] + i * m

    # If no solution
    return -1


def test(g, y, p):
    print("----By Baby Step Giant Step Algorithm-------")

    t0 = time.process_time_ns()
    print(baby_step_giant_step_dlp(g, y, p))

    t1 = time.process_time_ns() - t0
    print("Elapsed time(seconds) :", t1 * 10 ** -9)

    print("----By Naive Algorithm-------")
    t0 = time.process_time_ns()
    print(naive_dlp(g, y, p))
    t1 = time.process_time_ns() - t0
    print("Elapsed time(seconds) :", t1 * 10 ** -9)


if __name__ == '__main__':
    print("g^x = y (mod p)")
    print("x = log_g (y) (mod p)")
    # g, y, p = map(int, input("Enter g, y, p in space separated manner\n").split())
    print("Example\n ------")
    g = 5
    y = 21
    p = 23

    x = naive_dlp(g, y, p)
    print("By Naive Algorithm :", x)
    x = baby_step_giant_step_dlp(g, y, p)
    print("By BSGS Algorithm :", x)

    print("log_{} {} (mod {}) : {} ".format(g, y, p, x))

    # Uncomment to compare both algorithms in terms of execution time
    # test(497, 5751318998,5915587277)
    # test(7777, 719517368978140, 777737777777777)

    print("Question 1:\n ------")
    g = 3
    y = 326
    p = 881
    x = baby_step_giant_step_dlp(g, y, p)
    print("log_{} {} (mod {}) : {} ".format(g, y, p, x))

    print("Question 2:\n ------")
    g = 7
    y = 200
    p = 911
    x = baby_step_giant_step_dlp(g, y, p)
    print("log_{} {} (mod {}) : {} ".format(g, y, p, x))
