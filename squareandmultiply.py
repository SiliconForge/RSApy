def sam(base,expoente,modulo):
	binario = bin(expoente)
	produto = base
	for i in range (3,len(binario)):
		base = (base*base)%modulo
		if(binario[i] == '1'):
			base = (base*produto)%modulo
	return base
