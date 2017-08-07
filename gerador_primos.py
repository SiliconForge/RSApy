import random
from squareandmultiply import sam
def gerar_primo(nbits):
	while True:	
		candidato = random.randrange(pow(2,nbits-1),pow(2,nbits))
		if(candidato%2 != 0):
			break
	if(checar_primalidade(candidato)):
		return candidato
	return 0
def checar_primalidade(numero):
	r,u = achar_r(numero)
	for i in range (1,4):
		a = random.randrange(2,numero-1)
		z = sam(a,r,numero)
		if(z != 1 and z != numero-1):
			for j in range (1,u):
				z = (z*z)%numero
				if(z == 1):
					return False
			if(z != numero-1):
				return False
	return True
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
def gerar_n(nbits):
	tamanho = nbits
	while True:
		primop = gerar_primo(tamanho/2)
		if(primop != 0):
			break
	while True:
		primoq = gerar_primo(tamanho/2)
		if(primoq != 0):
			break
	N = primop*primoq
	return primop,primoq,N
