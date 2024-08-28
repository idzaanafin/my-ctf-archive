from Crypto.Util.number import long_to_bytes

n = 24820787846185217212923585921725266732934442848439471770031591287510465524369
e = 0x10
c = 9758402022762896120624828795976715802458243427749010727926795873222777042639
p = 12311069095640844691**2
q = 12797113224595654957**2

def legendre(a, p):
    return pow(a, (p - 1) // 4, p)
 
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
    r = pow(n, (q + 1) // 4, p)
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

def find_square_roots(c, e):
	if e == 1:
		flag = long_to_bytes(c)
#		if b"BEE" in flag:
		print(flag)
		return

	elif pow(c,(n-1)//2,n) != 1:
		return

	else:
		rt1 = tonelli(c, n)
		find_square_roots(rt1, e//4)
		rt2 = n - rt1
		find_square_roots(rt2, e//4)
	return

find_square_roots(c, e)
