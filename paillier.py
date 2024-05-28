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
    p = int(2147483647)
    q = int(1e9 + 7)
    n = p * q
    lmbda = lcm(p - 1, q - 1)

    # print(p, q, n, lmbda)

    g = random.randint(97, n**2 - 1)
    mu = pow(L(pow(g, lmbda, n ** 2), n), -1, n)

    return n, g, lmbda, mu


def encrypt(num, n, g):
    r = random.randint(1, n)
    c = (pow(g, num, n ** 2) * pow(r, n, n ** 2)) % (n ** 2) 
    return c


def decrypt(ecNum, n, lmbda, mu, g):
    m = (L(pow(ecNum, lmbda, n ** 2), n) * mu) % n
    return m

def add_encrypted_numbers(ecNum1, ecNum2, n):
    return ((ecNum1 * ecNum2) % (n**2))

def printVoteResult(numCandidates, dcResult):
    print("Vote result:")
    for candidate in range(1, numCandidates + 1):
        print(f"candidate{candidate}: {dcResult % 100}votes")
        dcResult //= 100

# # generate key pair
n, g, lmbda, mu = generate_keypair()

# num1 = int(input("num1: "))
# num2 = int(input("num2: "))

# encrypt
# ecNum1 = encrypt(num1, n, g)
# ecNum2 = encrypt(num2, n, g)
# ecSum = (ecNum1 * ecNum2) % (n**2)

# decrypt
# dcNum1 = decrypt(ecNum1, n, lmbda, mu, g)
# dcNum2 = decrypt(ecNum2, n, lmbda, mu, g)
# dcSum = decrypt(ecSum, n, lmbda, mu, g)


# print("num1(plain): {}".format(num1))
# print("num2(plain): {}".format(num2))

# print("num1(encrypted): {}".format(ecNum1))
# print("num2(encrypted): {}".format(ecNum2))
# print("ecSum: {}".format(ecSum))

# print("num1(decrypted): {}".format(dcNum1))
# print("num1(decrypted): {}".format(dcNum2))
# print("dcSum: {}".format(dcSum))

numCandidates = int(input("number of candidates (less than 10): "))
numVoters = int(input("number of voters (less than 999): "))

ecResult = encrypt(0, n, g)
for voter in range(numVoters):
    voteFor = int(input(f"Who do you want to vote (1 to {numCandidates}): "))
    voteNum = 100**(voteFor - 1)
    ecVoteNum = encrypt(voteNum, n, g)

    print(f"encrypted: {ecVoteNum}")
    ecResult = add_encrypted_numbers(ecResult, ecVoteNum, n)

dcResult = decrypt(ecResult, n, lmbda, mu, g)
print(dcResult)


printVoteResult(numCandidates, dcResult)

