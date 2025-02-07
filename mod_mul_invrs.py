def extended_gcd(a, b):
    """ Returns gcd(a, b) and the coefficients x, y such that ax + by = gcd(a, b) """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(m, n):
    """ Returns the modular inverse of m modulo n if it exists """
    gcd, x, _ = extended_gcd(m, n)
    
    if gcd != 1:
        return None  # Inverse does not exist if gcd(m, n) ≠ 1
    else:
        return x % n  # Ensuring a positive result

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("For {m} modulo {n}: ".format(m=m, n=n))

inverse = mod_inverse(m, n)

if inverse is None:
    print(f"Multiplicative inverse of {m} modulo {n} does not exist.")
else:
    print(f"Multiplicative inverse of {m} modulo {n} is {inverse}")