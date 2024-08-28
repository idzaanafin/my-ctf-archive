from sympy import totient
from libnum import *

exec(open('flag.txt','r').read())
p=246733235986476317472022632494207681507
q=299757821277872932404989514845667523387

#phi = totient(n)
phi = (p-1)*(q-1)
d = pow(e,-1,int(phi))

print(n2s(pow(c,d,n)))
