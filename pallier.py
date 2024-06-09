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
    p = 61  # 选择两个素数 p 和 q
    q = 53
    n = p * q
    lam = lcm(p - 1, q - 1)

    g = n + 1  # 选择 g，确保其阶为 n²
    mu = pow(L(pow(g, lam, n ** 2), n), -1, n)

    return n, g, lam, mu


def encrypt(m, n, g):
    r = random.randint(1, n)  # 生成随机数 r
    c = (pow(g, m, n ** 2) * pow(r, n, n ** 2)) % (n ** 2)  # 计算密文 c
    return c


def decrypt(c, n, lam, mu, g):
    m = (L(pow(c, lam, n ** 2), n) * mu) % n  # 解密得到明文 m
    return m


# 生成密钥对
n, g, lam, mu = generate_keypair()

# 要加密的明文
m = 5
a = 6
# 加密过程
c = encrypt(m, n, g)
b = encrypt(a, n, g)
# Homomorphic addition
c_plus_b = (c * b) % (n ** 2)

# Decrypt the result
decrypted_c_plus_b = decrypt(c_plus_b, n, lam, mu, g)

print("加密后的密文 c: {}".format(c))
print("加密后的密文 b: {}".format(b))
print("加密后的密文 c + b: {}".format(c_plus_b))
print("解密后的明文 c + b: {}".format(decrypted_c_plus_b))
# # 解密过程
# decrypted_m = decrypt(c, n, lam, mu, g)

# print("明文: {}".format(m))
# print("加密后的密文: {}".format(c))
# print("解密后的明文: {}".format(decrypted_m))