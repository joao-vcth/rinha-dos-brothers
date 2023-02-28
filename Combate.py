import random
import time

class Combate:
  @classmethod
  def calculo_de_dano(cls, jogador_um, jogador_dois, valor):
    jogadores = (jogador_um, jogador_dois)
    sorteio = random.choice(jogadores)
    sorteio.set_hp(sorteio.get_hp() - valor)
    print(f'O jogador {sorteio.get_nome()} recebeu {valor} de dano!\n')

  @classmethod
  def batalha(cls, jogador_um, jogador_dois):

    print(f'A batalha comecou! {jogador_um.get_nome()} vs {jogador_dois.get_nome()}\n')
    
    while jogador_um.get_hp() > 0 and jogador_dois.get_hp() > 0:
      critico = random.randint(0,40)
      dano = random.randint(0,40)
      if critico == dano:
         print("DANO CRITICO!!!")
         dano = 1000
      cls.calculo_de_dano(jogador_um, jogador_dois, dano)
      time.sleep(1)

      print(f'{jogador_um.get_nome()} tem {jogador_um.get_hp()} de HP - {jogador_dois.get_nome()} tem {jogador_dois.get_hp()} de hp \n')

    if jogador_um.get_hp() > jogador_dois.get_hp():
      print(f'{jogador_um.get_nome()} venceu!\n')
    if jogador_um.get_hp() < jogador_dois.get_hp():
      print(f'{jogador_dois.get_nome()} venceu!\n')