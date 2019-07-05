result = 0

for i in range(100, 1000):
	for j in range(100, 1000):
			auxiliar = str(i * j)
			if auxiliar == auxiliar[::-1] and int(auxiliar) > result:
				result = int(auxiliar)

print(result)