from libnum import *
#p = 221536023658397009003685500384711785303
#q = 307401687997526015954478984277755264899
#n = int((6.3%3.3+1.2+11**13/10.0+2**4.0*12.9+3%3.4%(11.3%9.6))) ^ 68100547624851099353845080557464606481352301262096425740474560492054242281096
#phi = (p-1)*(q-1)
#d = pow(65537,-1,phi)
#c = 542732316977950510497270190501021791757395568139126739977487019184541033966691938940926649138411381198426866278991473
#phi = c-1
#d = pow(65537,-1,c)
gatau=497288852047669908918399061102224148238007014539217284516523697620389622574310368171
#print(n2s(pow(gatau,d,c)^n))
print(gatau)
#m= pow(c,d,n)
#print(pow(pow(c,d,n),65537,n))
#print(pow(m,65537,n))
#print(n2s(pow(n,65537,gatau)))

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd == 1:
        return x % m
    else:
        raise ValueError("Modular inverse does not exist")

#modulus = 497288852047669908918399061102224148238007014539217284516523697620389622574310368171
#exponent = 65537
#phi_modulus = modulus - 1  # Assuming modulus is prime; for composite modulus, calculate φ(modulus)

# Compute modular inverse of exponent modulo φ(modulus)
#d = mod_inverse(exponent, phi_modulus)

#x = pow(result, d, modulus)
#result = 68100547624851099353845080557464606481352301262096425740474560488601979979397

# Compute x
#x = pow(result, d, modulus)

#print("Solution for x:", x)
from sympy import primefactors, mod_inverse

def modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)

def solve_modular_exponentiation(base, exponent, result):
    # Factorize the exponent into its prime factors
    prime_factors = primefactors(exponent)

    # List to store congruences (ai, ni) for CRT
    congruences = []

    # Solve each congruence modulo prime factors
    for p in prime_factors:
        ai = modular_exponentiation(base, exponent % (p - 1), p)
        ni = p
        bi = result % p
        congruences.append((ai, ni, bi))

    # Use Chinese remainder theorem (CRT) to solve the system of congruences
#    solution, modulus = crt(congruences)

    return congruences

# Example usage:
#base = 68100547624851099353845080557464606481352301262096425740474560488601979979397
#exponent = 65537
#result = 497288852047669908918399061102224148238007014539217284516523697620389622574310368171

#modulus = solve_modular_exponentiation(base, exponent, result)
#print("Modulus x:", modulus)

#print(pow(result,65537,x))
#print(n2s(x))
