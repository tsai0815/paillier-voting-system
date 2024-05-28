import random
import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def L(x, n):
    return (x - 1) // n


def generate_keypair():
    p = 61  
    q = 1e9+7
    n = p * q
    lam = lcm(p - 1, q - 1)

    g = n + 1 
    mu = pow(L(pow(g, lam, n ** 2), n), -1, n)

    return n, g, lam, mu


def encrypt(m, n, g):
    r = random.randint(1, n)
    c = (pow(g, m, n ** 2) * pow(r, n, n ** 2)) % (n ** 2) 
    return c


def decrypt(c, n, lam, mu, g):
    m = (L(pow(c, lam, n ** 2), n) * mu) % n
    return m

def add_encrypted_numbers(ecNum1, ecNum2, n):
    return (ecNum1 * ecNum2) % (n**2)

# # generate key pair
# n, g, lam, mu = generate_keypair()

# num1 = int(input("num1: "))
# num2 = int(input("num2: "))

# # encrypt
# ecNum1 = encrypt(num1, n, g)
# ecNum2 = encrypt(num2, n, g)
# ecSum = (ecNum1 * ecNum2) % (n**2)

# # decrypt
# dcNum1 = decrypt(ecNum1, n, lam, mu, g)
# dcNum2 = decrypt(ecNum2, n, lam, mu, g)
# dcSum = decrypt(ecSum, n, lam, mu, g)


# print("num1(plain): {}".format(num1))
# print("num2(plain): {}".format(num2))

# print("加密后的密文: {}".format(ecNum1))
# print("加密后的密文: {}".format(ecNum2))
# print("ecSum: {}".format(ecSum))

# print("解密后的明文: {}".format(dcNum1))
# print("解密后的明文: {}".format(dcNum2))
# print("dcSum: {}".format(dcSum))

numCandidates = int(input("number of candidates: "))
numVoters = int(input("number of voters: "))




