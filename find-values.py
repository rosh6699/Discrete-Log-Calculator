from math import ceil


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


if __name__ == '__main__':
    print("g^x = y (mod p)")
    print("x = log_g (y) (mod p)")
    g = 5
    y = 21
    p = 23
    # g, y, p = map(int, input("Enter g, y, p in space separated manner\n").split())

    secret = baby_step_giant_step_dlp(g, y, p)
    a = list(range(0, p))
    b = list(range(0, p))
    for i in a:
        for j in b:
            if i*j % (p - 1) == secret:
                print("a = {}, b = {} shared_key = {} ab = {}".format(i, j, pow(g,i*j,p),i*j))
    # for i in range(1, 22*22):
    #     if(pow(g,i,p) == 21):
    #         print(i)

