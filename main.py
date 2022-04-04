import Jogo
import Jogador

def CriarJogadores():
    nomeJogador1 = input('Insira nome do jogador 1: ')
    nomeJogador2 = input('Insira nome do jogador 2: ')

    jogador1 = Jogador.Jogador(nomeJogador1, 0)
    jogador2 = Jogador.Jogador(nomeJogador2, 0)
    return [jogador1, jogador2]

# Inicia os objetos do jogo
jogadores = CriarJogadores()
jogo = Jogo.Jogo(jogadores)

# Inicia Loop do jogo
jogo.LoopJogo()

print('OBRIGADO POR JOGAR!')






