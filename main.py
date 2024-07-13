from hero import Heroi
from monster import Monstro
from dado import Dado
import os, time

print("Bem vindo ao RPG teste")
print('Crie o seu personagem')

monstro = Monstro(10, 6)

nome = input("Nome do Personagem: ")
arma = input("Selecione o arco: ")
municao = input("Selecione o item flecha: ")

personagem = Heroi(nome, 10, 50, 0, arma, municao)

time.sleep(1)
os.system("cls")

print('''Na pacata vila de Verdan, 
um aventureiro sai a uma aventura por uma razão comum: 
uma mensagem de socorro enviada pela Grande Biblioteca de Eldoria. 
Essa biblioteca, conhecida por abrigar conhecimentos antigos e poderosos, 
estava sob a ameaça de forças sombrias.\n\n''')

time.sleep(1)
while monstro.vidaMonstro() > 0:
	print(f"O Monstro tem {monstro.vidaMonstro()} de vida.")

	print('''Você tem a opção de atirar com seu arco: Deseja? (S / N) ''')
	op = input("").upper()
	if op == 'S':
		dano_arco = Heroi.dano_heroi(personagem)
		monstro.abaixaVida(dano_arco)
		if monstro.vidaMonstro() == 0:
			break
		else:
			print(monstro.vidaMonstro())

	else:
		print("Você morre para o ogro")
		break
		
if monstro.vidaMonstro() <= 0:
	print("Você matou o monstro...")