from Crypto.Util.number import *
from secrets import n

flag = b'REDACTED'
print(len(flag))
p = getPrime(64)
q = getPrime(64)
m = int(flag.hex(), 0x10)
e = 65537
print(f'n = {n}')
print(f'e = {e}')
print(f'enkripsi = {pow(m, e, n)}') 