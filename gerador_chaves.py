from squareandmultiply import *
from fractions import gcd
import random
def campo_n_coprimos(p,q):
	phi = (p-1)*(q-1)
	return phi
def escolher_expoente(campo):
	final = 1000000
	if(campo < 1000000):
		final = campo
	while True:
		expoente = random.randrange(1,final)
		if(gcd(expoente,campo)==1):
			return expoente
	return 0
def escolher_chave_privada_deprecated(campo,expoente):
	for t in range (1,campo):
		chave_privada = (1+t*campo)/expoente
		if(chave_privada%1 == 0 and ((chave_privada*expoente)%campo == 1)):
			return chave_privada
	return 0
def escolher_chave_privada(campo,expoente):
	t=expoente
	while True:
		chave_privada = (1+t*campo)/expoente
		t = t+1
		if(chave_privada%1 == 0 and ((chave_privada*expoente)%campo == 1)):
			return chave_privada
	return 0
