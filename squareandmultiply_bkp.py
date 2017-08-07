def sam(base,expoente,modulo):
	binario = bin(expoente)
	produto = base
#	print "Numero binario para o expoente: " + str(binario)
#	print "Tamanho do vetor binario: " + str(len(binario))
	for i in range (3,len(binario)):
#		print "Binario posicao: " +str(i) + "  ->  " +str(binario[i])
		base = (base*base)%modulo
#		print "Base para posicao: " +str(i) + "  ->  " +str(base)
		if(binario[i] == '1'):
			base = (base*produto)%modulo
#			print "Base2 para posicao: " +str(i) + "  ->  " +str(base)
	return base
#print sam(input("Base: "),input("Expoente a gerar: "),10000000)
