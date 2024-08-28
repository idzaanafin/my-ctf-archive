import random
import numpy as np
import qrcode
from PIL import Image

def rescale(arr):
    mod = len(arr)
    final_arr = np.zeros(shape=(mod*10,mod*10), dtype=bool)
    for i in range(mod):
        for j in range(mod):
            final_arr[i*10:(i+1)*10, j*10:(j+1)*10] = arr[i][j]

    return final_arr

def mix(a,b,arr):
    mod = len(arr)
    narr = np.zeros(shape=(mod,mod), dtype=bool)
    for (x,y), element in np.ndenumerate(arr):
        nx = (x + y * a) % mod
        ny = (x * b + y * (a * b + 1)) % mod

        narr[nx][ny] = element

    return narr

def inverse_rescale(arr):
    mod = len(arr) // 10
    final_arr = np.zeros(shape=(mod, mod), dtype=bool)
    for i in range(mod):
        for j in range(mod):
            final_arr[i][j] = np.any(arr[i * 10:(i + 1) * 10, j * 10:(j + 1) * 10])

    return final_arr


i = 0
for a in range(21):
	for b in range(21):
		scrambled_img = Image.open('mixed.png')
		scrambled_arr = np.array(scrambled_img)
		scrambled=inverse_rescale(scrambled_arr)
		for _ in range(26):
			scrambled = mix(a,b,scrambled)

		scrambled = rescale(scrambled)
		img = Image.fromarray(scrambled)
		img.save(f'{i}.png')
		i+=1
		print(a,b)
