from squareandmultiply import *
def crypto(texto,expoente,campo_n):
	mensagem = sam(texto,expoente,campo_n)
	return mensagem
def decrypto(texto,chave,campo_n):
	mensagem = sam(texto,chave,campo_n)
	return mensagem
