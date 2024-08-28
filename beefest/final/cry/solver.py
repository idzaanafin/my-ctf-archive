
from libnum import *
def egcd(a, b):
    # extended Euclidean algorithm
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def find_square_roots(c, n, e):
    if e == 1:
        return [c]

    elif pow(c, (n - 1) // 2, n) != 1:
        return []

    else:
        rt1 = tonelli(c, n)
        res1 = find_square_roots(rt1, n, e // 2)
        rt2 = n - rt1
        res2 = find_square_roots(rt2, n, e // 2)
        return res1 + res2

from Crypto.Util.number import long_to_bytes


n = 24820787846185217212923585921725266732934442848439471770031591287510465524369
e = 0x10
ct = 9758402022762896120624828795976715802458243427749010727926795873222777042639
p = 12311069095640844691**2
q = 12797113224595654957**2

_, m1, m2 = egcd(p, q)
a1 = ct % p
a2 = ct % q
sq_a1 = [nroot(a1,16)] #find_square_roots(a1, n, 16)
sq_a2 = [nroot(a1,16)] #find_square_roots(a2, n, 16)
print(sq_a1)
for s in sq_a1:
    assert pow(s, 16, p) == a1
print(sq_a2)
for s in sq_a2:
    assert pow(s, 16, q) == a2

new_sq = sq_a1[0] * m2 * q + sq_a2[0] * m1 * p
new_sq = new_sq % n
print(new_sq)
assert pow(new_sq, 16, n) == c
print(long_to_bytes(new_sq))
