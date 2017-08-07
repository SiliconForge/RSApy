from gerador_primos import *
from gerador_chaves import *
from crytodecrypto import *
from converttext import *
from PySide.QtGui import *

reso_x = 1360
reso_y = 768

class fechar(object):
	def __init__(self,button):
		self.button = button
	def fechares(self):
		app.quit()

app = QApplication([])
window = QWidget()
gui = QWidget()
saize,ok = QInputDialog.getText(gui,"Tamanho da chave: ", "Entre com o tamanho da chave") 
pe,qe,ene = gerar_n(int(saize))
print "\nNumero primo P: " + str(pe) + " ----> em [" +str(len(bin(pe))-2)+ "] bits : " + bin(pe)
print "\nNumero primo Q: " + str(qe) + " ----> em [" +str(len(bin(qe))-2)+ "] bits : " + bin(qe)
print "\nCampo N: " + str(ene)  + " ----> em [" +str(len(bin(ene))-2)+ "] bits : " + bin(ene)
coprimos = campo_n_coprimos(pe,qe)
print "\nCoprimos no campo: " + str(coprimos) + " ----> em [" +str(len(bin(coprimos))-2)+ "] bits : " + bin(coprimos)
expoente_publico = escolher_expoente(coprimos)
print "\nExpoente publico: " + str(expoente_publico) + " ----> em [" +str(len(bin(expoente_publico))-2)+ "] bits : " + bin(expoente_publico)
chave_privada = escolher_chave_privada(coprimos,expoente_publico)
print "\nChave privada: " + str(chave_privada) + " ----> em [" +str(len(bin(chave_privada))-2)+ "] bits : " + bin(chave_privada) + "\n"
arquivo_chave_publica = open("chave_publica.key","w+")
arquivo_chave_publica.write(str(expoente_publico)+ "\n" + str(ene))
arquivo_chave_privada = open("chave_privada.key","w+")
arquivo_chave_privada.write(str(chave_privada))
texteF = open("texto_pleno.txt","r")
texte = int(texttoint(texteF.read()))
ctexte = crypto(texte,expoente_publico,ene)
ctexteF = open("texto_cifrado.txt","w+")
ctexteF.write(str(ctexte))
dtexte = inttotext(decrypto(ctexte,chave_privada,ene))
dtexteF = open("texto_decodificado.txt","w+")
dtexteF.write(dtexte)
label_P = QLabel("Numero primo P: " + str(pe),window)
label_Q = QLabel("Numero primo Q: " + str(qe),window)
label_N = QLabel("Campo N: " + str(ene),window)
label_Co = QLabel("Coprimos no campo: " + str(coprimos),window)
label_E = QLabel("Expoente publico: " + str(expoente_publico),window)
label_Cp = QLabel("Chave privada: " + str(chave_privada),window)
label_Q.move(0,label_P.frameGeometry().height()*1)
label_N.move(0,label_P.frameGeometry().height()*2)
label_Co.move(0,label_P.frameGeometry().height()*3)
label_E.move(0,label_P.frameGeometry().height()*4)
label_Cp.move(0,label_P.frameGeometry().height()*5)
button = QPushButton("Exit",window)
sair = fechar(button)
button.clicked.connect(sair.fechares)
button.move(0,label_P.frameGeometry().height()*6)
window.setGeometry((reso_x/4),(reso_y/4),(reso_x/2),(reso_y/2))
#window.resize(500,200)
window.show()
app.exec_()
