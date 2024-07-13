import random

class Heroi:
	def __init__(self, nome, vida, mana, xp, item_primario, item_secundario) -> None:
		self.nome = nome
		self.vida = vida
		self.mana = mana
		self.xp = xp
		self.qtn_municao = random.randint(1, 10)
		self.item_primario = item_primario
		self.item_secundario = item_secundario

	def nomePersonagem(self):
		return self.nome
	
	def vidaPersonagem(self):
		return self.vida
	
	def manaPersonagem(self):
		return self.mana

	def xpPersonagem(self):
		return self.xp

	def itemPrimario(self):
		if self.item_primario == 'arco':
			pass
		
	def itemSecundario(self):
		if 'flecha':
			return 'flecha'
		
	def qntMunicao(self):
		return self.qtn_municao
	
	def dano_heroi(self):
		if self.item_primario == 'arco':
			dano = random.randint(1, 6)
			return dano