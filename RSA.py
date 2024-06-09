import random
import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b // a) * x, x


def generate_keypair():
    p = 61  # 选择两个素数 p 和 q
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # 选择一个公开的 e
    d = modinv(e, phi)  # 计算 d，使得 ed ≡ 1 (mod phi)

    return (e, n), (d, n)


def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext


def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

def check(blinding_factor, private_key):
    try:
        a = pow(blinding_factor, -1, private_key)
    except:
        return False
    return True

def blinding(public_key, m):

    blinding_factor = random.randint(1, 1000)
    while(check(blinding_factor, private_key) == False):
        blinding_factor = random.randint(1, 1000)
    blind_m = m * pow(blinding_factor, public_key[0]) % public_key[1]
    return (blinding_factor, blind_m)
def signature(private_key, blind_m):
    signature = pow(blind_m, private_key[0], private_key[1])
    return signature
def unblind(public_key, private_key, signature, blinding_factor):
    unblinded_signature = (signature * pow(blinding_factor, -1, public_key[1])) % public_key[1]
    return unblinded_signature

# 生成密钥对
public_key, private_key = generate_keypair()

# 要加密的明文
m = 42
blinding_factor, blind_m = blinding(public_key, m)
#signature = signature(private_key, blind_m)
print("加密后的密文 c: {}".format(signature))
#unblinded_signature = unblind(public_key, private_key, signature, blinding_factor)
#print("解密后的明文: {}".format(unblinded_signature))
# 加密过程
# c = encrypt(public_key, m)
# print("加密后的密文 c: {}".format(c))

# # 解密过程
# decrypted_m = decrypt(private_key, c)
# print("解密后的明文: {}".format(decrypted_m))
