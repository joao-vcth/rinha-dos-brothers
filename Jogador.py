class Jogador:
  
  def __init__(self, nome):
    self.hp = 150
    self.nome = nome
    print(f'Novo jogador {self.get_nome()} foi criado com {self.get_hp()} de HP\n')

  def get_atq(self):
    return self.atq

  def get_defesa(self):
    return self.defesa

  def get_hp(self):
    return self.hp

  def get_nome(self):
    return self.nome
    
  def set_atq(self, valor):
    self.atq = valor

  def set_defesa(self, valor):
    self.defesa = valor

  def set_hp(self, valor):
    self.hp = valor

  def set_nome(self, novo_nome):
    self.nome = novo_nome

  def __repr__(self):
    return self.nome