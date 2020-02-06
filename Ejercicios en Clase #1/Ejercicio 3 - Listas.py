a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
b = [1, 5, 77, 22, 90, 25, 83, 100, 2, 21, 90]
c=[]
d = len(b)

for i in a:
	contador = 0
		for x in b:
			contador +=1
			if x=i:
				break
			if contador ==d-1:
				c.append(i)

print(c)