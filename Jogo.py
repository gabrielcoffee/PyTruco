import random
import Carta

class Jogo():
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.manilha = 0
        self.tentosRodada = 1
        self.terminarRodada = False

    def LoopJogo(self):
        continuarJogo = True

        # Continua loop do jogo se nenhum dos jogadores possui 12 tentos
        while continuarJogo:
            self.MostrarPlacar()
            self.LoopRodada()
            continuarJogo = self.jogadores[0].tentos < 12 and self.jogadores[1].tentos < 12

        # Confere qual dos jogadores venceu o jogo
        for jogador in self.jogadores:
            if (jogador.tentos >= 12):
                vencedorJogo = jogador

        print(vencedorJogo, 'VENCEU O JOGO TRUCO!!!')

    def LoopRodada(self):
        continuarRodada = True
        self.DistribuirCartas(self.CriarCartas())

        # Continua loop da rodada se nenhum dos jogadores possui 2 pontos
        while continuarRodada:

            # Roda a vez de cada jogador
            for jogador in self.jogadores:
                self.EscolherAcao(jogador)

                if (self.terminarRodada):
                    break
            if (self.terminarRodada):
                break

            # Confere quem venceu o turno e atribui os pontos
            vencedor = self.QuemVenceuTurno()
            vencedor.pontosRodada += 1
            self.RemoverCartasUsadas()
            print(vencedor.nome, 'venceu o turno com um', vencedor.cartaAtual.NomeInteiro())
            print()

            continuarRodada = self.jogadores[0].pontosRodada < 2 and self.jogadores[1].pontosRodada < 2

        if (self.terminarRodada == False):
            vencedorRodada = self.QuemVenceuRodada()
            vencedorRodada.tentos += self.tentosRodada
            print('Fim da rodada!', vencedorRodada.nome, 'levou', self.tentosRodada, 'tento')

        # Zera os pontos da rodada
        for j in self.jogadores:
            j.pontosRodada = 0

    def QuemVenceuRodada(self):
        # Retorna qual dos jogadores venceu a rodada e zera os pontos de ambos
        vencedor = 0
        for jogador in self.jogadores:
            if (jogador.pontosRodada >= 2):
                vencedor = jogador
            jogador.pontosRodada = 0
        if (vencedor == 0):
            return
        else:
            return vencedor

    def EscolherAcao(self, jogador):
        print('É a vez de', jogador.nome)
        acao = input('Escolha a ação (jogar/trucar): ')

        if (acao == 'jogar'):
            self.EscolherCarta(jogador)
        elif (acao == 'trucar'):
            self.JogoTrucado(jogador)
        else:
            print('Comando inválido, tente novamente')
            self.EscolherAcao(jogador)

    def EscolherCarta(self, jogador):
        jogador.PrintOpcoesCartas()
        opcao = int(input('Qual carta vai jogar? '))
        cartaInvalida = True

        # Define se carta é foi válida e seleciona como carta atual do jogador
        for carta in jogador.cartas:
            if (carta.id == opcao):
                cartaInvalida = False
                jogador.cartaAtual = carta
                print(jogador.nome, 'jogou um', carta.NomeInteiro())
                print()

        # Roda a função novamente se carta foi inválida
        if (cartaInvalida == True):
            print()
            print('Carta inválida, tente novamente.')
            self.EscolherCarta(jogador)

    def JogoTrucado(self, jogadorTrucou):
        # Define quem recebeu a trucada
        for j in self.jogadores:
            if (j != jogadorTrucou):
                outroJogador = j

        if (self.tentosRodada == 1): msg = 'TRUUCO!!!'
        if (self.tentosRodada == 3): msg = 'SEEEIS!!!'
        if (self.tentosRodada == 6): msg = 'NOOOVE!!!'
        if (self.tentosRodada == 9): msg = 'DOOOZE!!!'

        print(jogadorTrucou.nome, 'pediu', msg)
        print()
        print('É a vez de', outroJogador.nome)
        acao = input('Escolha a ação (aceitar/correr/aumentar): ')

        if (acao == 'aceitar'):
            if (self.tentosRodada == 1): self.tentosRodada = 3
            else: self.tentosRodada += 3
            self.EscolherCarta(outroJogador)
        elif (acao == 'correr'):
            self.terminarRodada = True
            jogadorTrucou.tentos += self.tentosRodada
            print('Fim da rodada!', jogadorTrucou.nome, 'levou', self.tentosRodada, 'tento')
            print()
            return


    def RemoverCartasUsadas(self):
        for jogador in self.jogadores:
            jogador.cartas.remove(jogador.cartaAtual)

    def DistribuirCartas(self, cartas):
        maxCartas = 3
        id = 1

        # Passa por todos os jogadores, escolhe uma carta aleatória,
        # entrega ao jogador e a remove da lista, depois seleciona a manilha
        for jogador in self.jogadores:
            print('\n', jogador.nome, ' recebeu as cartas:', sep='')
            while id < maxCartas + 1:
                cartaEscolhida = random.choice(cartas)
                jogador.cartas.append(cartaEscolhida)
                cartas.remove(cartaEscolhida)
                cartaEscolhida.DefinirId(id)
                print(cartaEscolhida.NomeInteiro())
                id += 1

            id = 1

        self.manilha = random.choice(cartas)
        print()
        print('Manilha são as cartas: ', self.manilha.NomeValor())

    def CriarCartas(self):
        valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        naipes = [1, 2, 3, 4]
        listaCartas = []

        # Cria todas as cartas possíveis (40) e adiciona a lista
        for valor in valores:
            for naipe in naipes:
                carta = Carta.Carta(valor, naipe)
                listaCartas.append(carta)
        return listaCartas

    def QuemVenceuTurno(self):
        # Ainda posso simplificar esse código, mas funciona

        carta1 = self.jogadores[0].cartaAtual
        carta2 = self.jogadores[1].cartaAtual

        print(carta1)
        print(carta2)

        # Os 2 jogadores possuem manilha, decide no naipe
        if (carta1.valor  == carta2.valor == self.manilha):
            if (carta1.naipe > carta2.naipe):
                return self.jogadores[0]
            else:
                return self.jogadores[1]

        # Empatou e nenhum possui manilha (empate ainda não funciona 02/04/22)
        elif (carta1.valor == carta2.valor != self.manilha):
            return 0

        # Cartas diferentes, ganha a maior, mas perde se a outra for manilha
        elif (carta1.valor > carta2.valor):
            if (carta2 != self.manilha):
                return self.jogadores[0]
            else:
                return self.jogadores[1]
        elif (carta1.valor < carta2.valor):
            if (carta1.valor != self.manilha):
                return self.jogadores[1]
            else:
                return self.jogadores[0]

    def MostrarPlacar(self):
        jogador1 = self.jogadores[0]
        jogador2 = self.jogadores[1]

        print('O jogo está:', jogador1.nome, jogador1.tentos, 'X', jogador2.tentos, jogador2.nome)