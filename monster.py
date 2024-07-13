import random

class Monstro:
	def __init__(self, vida, dado_boss) -> None:
		self.vida = vida
		self.dado = 0
		self.dado_boss = dado_boss

	def nomeMonstro(self):
		return self.nome
	
	def vidaMonstro(self):
		if self.vida <= 0:
			return 0

		else:
			return self.vida
	
	def manaMonstro(self):
		return self.mana
	
	def dadoDano(self):
		self.dado = random.randint(1, self.dado_boss)
		return self.dado
	
	def abaixaVida(self, dano):
		self.vida -= dano
