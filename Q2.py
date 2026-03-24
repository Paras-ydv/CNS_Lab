# DES Encryption/Decryption
# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate key
def generate_key():
    return get_random_bytes(8)

# Encrypt
def encrypt(key, data):
    cipher = DES.new(key, DES.MODE_CBC)
    encrypted = cipher.encrypt(pad(data, 8))
    return cipher.iv, encrypted

# Decrypt
def decrypt(key, iv, encrypted_data):
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(encrypted_data), 8)

# -------- MAIN --------
key = generate_key()
print("Key:", key)

message = input("Enter message: ").encode()

iv, encrypted = encrypt(key, message)
print("Encrypted:", encrypted)

decrypted = decrypt(key, iv, encrypted)
print("Decrypted:", decrypted.decode())