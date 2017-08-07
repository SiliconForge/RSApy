def texttoint(texto):
	linha = ""
	for i in range (0,len(texto)):
		caractere = texto[i]
#		print caractere
		linha = linha + bin(ord(caractere))[2:]
#		print linha
	numero = int(linha,2)
	return numero


def inttotext(inteiro):
	linha = ""
	binario = bin(inteiro)[2:]
#	print binario
	for i in range (0,len(binario),7):
		bina = binario[i:i+6]
#		print bina
		caractere = chr(int(binario[i:i+7],2))
#		print caractere
		linha = linha + caractere
	return linha

#print texttoint("aqui_eh_curintia",0)
#print inttotext(3970890316005641268429397266609377,0)
