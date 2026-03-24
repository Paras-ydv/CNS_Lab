# Power function (same recursive logic as C)
def power(a, b, mod):
    if b == 1:
        return a % mod
    
    t = power(a, b // 2, mod)
    
    if b % 2 == 0:
        return (t * t) % mod
    else:
        return ((t * t) % mod * a) % mod


# Calculate key (same as C function)
def calculate_key(a, x, n):
    return power(a, x, n)


# -------- MAIN --------
n = int(input("Enter the value of n (prime): "))
g = int(input("Enter the value of g (generator): "))

# First person (Alice)
x = int(input("Enter private key x for first person: "))
a = power(g, x, n)

# Second person (Bob)
y = int(input("Enter private key y for second person: "))
b = power(g, y, n)

# Shared keys
key1 = power(b, x, n)
key2 = power(a, y, n)

print("Key for first person:", key1)
print("Key for second person:", key2)