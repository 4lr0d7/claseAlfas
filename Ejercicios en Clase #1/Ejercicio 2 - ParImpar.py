"""print("Programa que te ayuda a saber si un número es par o impar")
num = int(input("Inserte un valor (NOTA: Debe de ser positivo): "))
 contador = 0

if num%2==0:
	print("Tu número es par")
elif num%2!=0:
	for i in range (2, num+1):
		if(num%i)==0:
			contador+=1
		if contador == 2:
			print("el número es primo")
		elif contador>2:
			print("el número no es primo") """

numero = int(input("Ingresa algún número: "))

if (numero%2 ==0):
	print("Tú número es par")
else:
	print("Tú número es impar")
