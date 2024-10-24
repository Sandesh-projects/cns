import random
from math import gcd

def mod_inverse(a, m):
    """Finds the modular inverse of a with respect to m."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def is_prime(n):
    """Checks if a number n is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    """Generates a random prime number with a specified number of bits."""
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def generate_key(bits):
    """Generates a pair of public and private keys."""
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(e, phi_n) == 1:
            break

    d = mod_inverse(e, phi_n)
    
    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    """Encrypts a plaintext message using the public key."""
    e, n = public_key
    return pow(plaintext, e, n)

def decrypt(ciphertext, private_key):
    """Decrypts a ciphertext message using the private key."""
    d, n = private_key
    return pow(ciphertext, d, n)


public_key, private_key = generate_key(8)

plaintext = 42
ciphertext = encrypt(plaintext, public_key)
decrypted_msg = decrypt(ciphertext, private_key)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_msg}")