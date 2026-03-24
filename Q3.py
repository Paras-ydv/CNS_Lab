# RSA Implementation in Python (without OOP)

import math

# GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Key generation
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # Modular inverse (fast)
    d = pow(e, -1, phi)

    return (e, n), (d, n)

# Encrypt
def encrypt(public_key, message):
    e, n = public_key
    return [pow(ord(ch), e, n) for ch in message]

# Decrypt
def decrypt(private_key, cipher):
    d, n = private_key
    return ''.join(chr(pow(c, d, n)) for c in cipher)

# -------- MAIN --------
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

public_key, private_key = generate_keys(p, q)

print("Public Key:", public_key)
print("Private Key:", private_key)

msg = input("Enter message: ")

cipher = encrypt(public_key, msg)
print("Encrypted:", cipher)

plain = decrypt(private_key, cipher)
print("Decrypted:", plain)