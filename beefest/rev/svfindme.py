from Crypto.Util.number import *

v1 = long_to_bytes(0x4F64677572757576)[::-1]
v2 = long_to_bytes(0x5F085F6B08510460)[::-1]
v3 = long_to_bytes(0x59546B044709566B)[::-1]
v4 = long_to_bytes(0xB455F596B445548)[::-1]
v5 = long_to_bytes(77)

for i in range(33):
      print(chr(((((v1+v2+v3+v4+v5)[i]+0)-2)^0x36)%255),end='')
