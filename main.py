from Jogador import Jogador
from Combate import Combate

dict_de_jogadores = {}

def lista_de_jogadores():
  
  id_do_jogador = 1
  
  while True:
    nome = str(input("Digite o nome do seu jogador para cria-lo: "))
    jogador = Jogador(nome)
    opcao = str(input("Deseja criar outro jogador? S/N ")).upper()

    while len(opcao) != 1 or opcao not in 'SN':
      print("Opcao invalida.")
      opcao = str(input("Deseja criar outro jogador? S/N ")).upper()
    
    if opcao == "N":
      dict_de_jogadores[id_do_jogador] = jogador
      break
    if opcao == "S":
      dict_de_jogadores[id_do_jogador] = jogador
      id_do_jogador += 1
      
def seleciona_jogador(jogadores):
  
  jogadores_dict = jogadores

  for id, jogador in dict_de_jogadores.items():
    print(f'{id} : {jogador}')
    
  selecao = int(input(f'Selecione o seu jogador: \n'))
  print(f'Voce escolheu {jogadores[selecao].get_nome()}')
  return jogadores_dict[selecao]

def main():
  lista_de_jogadores()

  batalha = Combate()
  selecao1 = seleciona_jogador(dict_de_jogadores)
  selecao2 = seleciona_jogador(dict_de_jogadores)
  batalha.batalha(selecao1, selecao2)


main()
print("Fim.")