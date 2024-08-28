enc = open('not_key','rb').read()

something = b'angin_topan'


s = 100
v6 = 't'
v7 = 111
#v8 =
v9 = 105
v10 = 'e'

v7-=6
v5 = v7+6
v5 = 105
s = v5 +10
s = 100
v1 = 108
v9 = 65
v2 = s * 7 -1 +7
v8 = something[8] -3

flag = [i for i in range(1,8)]
flag[0] = 115 # sama dengan s
flag[1] = 111 # sama dengan v5
flag[2] = ord('t') #sama dengan v6
flag[3] = 111 # sama dengan v7
flag[4] =  v8 # sama dengan v8
flag[5]= 105 #sama dengan v9
flag[6] = ord('e') #sama dengan v10

print(''.join([chr(flag[i]) for i in range(7)]))
