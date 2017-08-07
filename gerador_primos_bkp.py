import random
from squareandmultiply import sam
def gerar_primo(nbits):
	while True:	
		candidato = random.randrange(pow(10,nbits-1),pow(10,nbits))
		if(candidato%2 != 0):
			break
	if(checar_primalidade(candidato)):
		return candidato
	return 0

def checar_primalidade(numero):
	r,u = achar_r(numero)
#	print "numero U: " + str(u)
#	print "numero R: " + str(r)
	for i in range (1,4):
		a = random.randrange(2,numero-1)
#		print "numero a: " + str(a)
#		z = power(a,r)%numero
		z = sam(a,r,numero)
#		print "numero z1: " + str(z)
		if(z != 1 and z != numero-1):
#			print "numero z2: " + str(z)
			for j in range (1,u):
				z = (z*z)%numero
#				print "numero z3: " + str(z)
				if(z == 1):
					return False
			if(z != numero-1):
#				print "numero z4: " + str(z)
				return False
	return True

#				print "numero a: " + str(a)
#				print "numero z: " + str(z)
		
def achar_r(numero):
	numero = numero-1
	u=0
	while True:
		numero = numero/2
		u = u+1
		if((numero/2)%1 == 0):
			if(numero%2 ==0):
				continue
			else:
				break
	return numero,u
'''
def power(b,p):
    """
    Calculates b^p
    Complexity O(log p)
    b -> double
    p -> integer
    res -> double
    """
    res = 1

    while p:
        if p & 0x1: res *= b
        b *= b
        p >>= 1

    return res
'''
#print achar_r(45)
#for i in range (5,200):
#	if(checar_primalidade(i)):
#		print i
#print checar_primalidade(input("Coloque um primo a testar: "))
tamanho = input("Tamanho do numero N: ")
while True:
	primop = gerar_primo(tamanho/2)
	if(primop != 0):
		break
print "Primo P: " + str(primop)
while True:
	primoq = gerar_primo(tamanho/2)
	if(primoq != 0):
		break
print "Primo Q: " + str(primoq)
print "Numero N: " + str(primop*primoq)
