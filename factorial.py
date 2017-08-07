def factorial(numero):
	resultado = 1
	for i in range (1,numero+1):
		resultado = resultado * i
#		if(i%1000 == 0):
#			print i
	return resultado
print factorial(input("Numero:  "))
