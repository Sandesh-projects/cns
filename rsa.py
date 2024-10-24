import random
from math import gcd

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a//m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def is_prime(n):
    if n <= 1:
        return False
    elif n<=3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i*i <= n :
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p
            

def generate_key(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n= p * q
    phiN = (n-1)*(q-1)

    while True:
        e = random.randint(1, 100000)
        if gcd(e, phiN) == 1:
            break
    
    d = mod_inverse(e, phiN)
    
    return (e, n), (d, n)

def encrypt(plainterxt, public_key):
    e, n = public_key
    return pow(plainterxt, e, n)

def decrypt(ciphertext, private_key):
    d, n =private_key

    return pow(ciphertext, d, n)

    
public_key , Private_key = generate_key(8)

plainterxt = 42
ciphertext = encrypt(plainterxt, public_key)
decrypted_msg = decrypt(ciphertext, Private_key)

print(f"Public Key: {public_key}")
print(f"Private Key: {Private_key}")
print(f"Plaintext: {plainterxt}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_msg}")
