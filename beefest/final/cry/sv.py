from math import isqrt
from egcd import egcd
from libnum import *
#exec(open('hasil.txt','r').read())

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    return p, q

n = 24820787846185217212923585921725266732934442848439471770031591287510465524369
e = 0x10

ct = 9758402022762896120624828795976715802458243427749010727926795873222777042639
phi 24820787846185217208967888585882082909717237852184525012501212523772123024680
p = 12311069095640844691**2
q = 12797113224595654957**2

_,yp,yq= egcd(p,q)
#for i in [2,4,6,8,10,12,14,16,18,32]:
#	for j in [2,4,6,8,10,12,14,16,18,32]:
mp = pow(ct, (p+1)//16, p)
mq = pow(ct, (q+1)//16, q)
print(n2s(mp))
print(n2s(mq))

r = (yp*p*mq + yq*q*mp) %n
mr = n - r
s = (yp*p*mq - yq*q*mp) %n
ms = n - s
for num in [r,mr,s,ms]:
	    print(n2s(num))


