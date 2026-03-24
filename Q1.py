text = input("Enter plain text: ")
key = int(input("Enter key: "))

# Encryption
cipher = ""
for ch in text:
    if ch.isalpha():
        shift = 65 if ch.isupper() else 97
        cipher += chr((ord(ch) - shift + key) % 26 + shift)
    else:
        cipher += ch

print("Encrypted text:", cipher)

# Decryption
plain = ""
for ch in cipher:
    if ch.isalpha():
        shift = 65 if ch.isupper() else 97
        plain += chr((ord(ch) - shift - key) % 26 + shift)
    else:
        plain += ch

print("Decrypted text:", plain)