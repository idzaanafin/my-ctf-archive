from Crypto.Util.number import getPrime, getRandomNBitInteger

class ENCG:
    def __init__(self):
        self.a = getPrime(16)
        self.b = getPrime(16)
        self.c = getPrime(16)
        self.state = getRandomNBitInteger(8)
    def next(self):
        self.state = self.a * self.state**2 + self.b*self.state + self.c
        return self.state
    
menu = """1. Grow Pokexpon
2. Battle Pokexpon"""
rng = ENCG()
while True:
    print(menu)
    choice = int(input(">> "))
    if choice == 1:
        print("Your Pokexpon is growing...")
        power = rng.next()
        print("Your Pokexpon's power is", power)
    elif choice == 2:
        print("Your Pokexpon is battling...")
        print("Your Pokexpon won!")
        print("If you can guess the secret, you will also get flag")
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        if a == rng.a and b == rng.b and c == rng.c:
            print("Congrats, here is your flag")
            print(open("flag.txt").read())
        else:
            print("Wrong secret, no flag :(")
    else:
        print("Invalid choice")
