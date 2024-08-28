from Crypto.Util.number import *

class ENCG:
    def __init__(self):
        self.a = getPrime(16)
        self.b = getPrime(16)
        self.c = getPrime(16)
        self.state = getRandomNBitInteger(8)
    def next(self):
        self.state = self.a * self.state**2 + self.b*self.state + self.c
        return self.state


#next state is ax2+bx+c we know the x from before state
# a bisa didapat dari next_state//befstate**2

state = 1517046357
secret = 150142968986815986965257
a = secret//(state**2)
for i in range(9999,999999):
	a2spbs = (secret - i)
	bs = a2spbs-(a*(state**2))
	b = bs//state
	if (a*pow(state,2))+(b*state)+i == secret:
		print(a,b,i)
		break

