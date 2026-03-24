import math

# GCD
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Key generation
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = pow(e, -1, phi)

    return (e, n), (d, n)

# Encrypt (character output)
def encrypt(public_key, message):
    e, n = public_key

    cipher_chars = ""
    cipher_nums = []

    for c in message:
        enc = pow(ord(c), e, n)
        cipher_nums.append(enc)

        # convert safely to char
        cipher_chars += chr(enc % 256)

    print("Encrypted (chars):", cipher_chars)
    return cipher_nums   # IMPORTANT for decryption

# Decrypt
def decrypt(private_key, cipher):
    d, n = private_key
    return ''.join(chr(pow(c, d, n)) for c in cipher)

# -------- MAIN --------
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

public_key, private_key = generate_keys(p, q)

print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

msg = input("Enter message: ")

cipher = encrypt(public_key, msg)

plain = decrypt(private_key, cipher)
print("Decrypted:", plain)