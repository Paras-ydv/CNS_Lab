import hashlib

# Function to convert bytes to hex (like Java bytesToHex)
def bytes_to_hex(byte_data):
    return ''.join(format(b, '02x') for b in byte_data)

try:
    print("Message Digest Info:")

    # Python equivalent of MessageDigest.getInstance("SHA1")
    print("Algorithm = SHA-1")
    print("Provider = hashlib (Python built-in)")
    print()

    # First input
    input_text = ""
    hash_obj = hashlib.sha1()
    hash_obj.update(input_text.encode())
    output = hash_obj.digest()
    print(f'SHA1("{input_text}") = {bytes_to_hex(output)}')
    print()

    # Second input
    input_text = "abc"
    hash_obj = hashlib.sha1()
    hash_obj.update(input_text.encode())
    output = hash_obj.digest()
    print(f'SHA1("{input_text}") = {bytes_to_hex(output)}')
    print()

    # Third input
    input_text = "abcdefghijklmnopqrstuvwxyz"
    hash_obj = hashlib.sha1()
    hash_obj.update(input_text.encode())
    output = hash_obj.digest()
    print(f'SHA1("{input_text}") = {bytes_to_hex(output)}')
    print()

except Exception as e:
    print("Exception:", e)