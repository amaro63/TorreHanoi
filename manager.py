import os
from disco import disco
from pino import pino
from display import display
from os.path import exists
import json

class manager:

    # # # # # # # # # # # # # # # # # # # # # #
    #
    # ctor
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, min, max):
        self.nomeArquivo = "saved.json"
        self.imp = display()
        self.discos = []
        self.gameOver = False
        self.numMovimentos = 0
        self.carregouGame = self.recuperarGame()
        if not self.carregouGame:
            self.numDiscos = self.obterNumeroDiscos(min, max)
            self.inicializaPinosDiscos()
            for i in range(self.numDiscos):
                self.pinos[0].empilharDisco(self.discos[self.numDiscos-1-i])


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # inicializaPinosDiscos()
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def inicializaPinosDiscos(self):
        self.p1 = pino(self.numDiscos)
        self.p2 = pino(self.numDiscos)
        self.p3 = pino(self.numDiscos)
        self.pinos = [self.p1, self.p2, self.p3]
        for i in range(self.numDiscos):
            self.discos.append(disco(1+2*(i+1)))


    # # # # # # # # # # # # # # # # # # # # # #
    #
    #  obterNumeroDiscos
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def obterNumeroDiscos(self, min, max):
        discos = 0
        while not discos in range(min, max+1):
            try:
                discos = int(input(f"Quantos discos ({min} a {max})? "))
            except:
                print("Valor inválido.")
        return discos


    # # # # # # # # # # # # # # # # # # # # # #
    #
    #  obterRespostaSN
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def obterRespostaSN(self, msg):
        resposta = ""
        while not resposta in ['s','n']:
            try:
                resposta = input(msg)
            except:
                print("Algo deu errado...")
                input("<Enter>")
        return (resposta == 's')


    # # # # # # # # # # # # # # # # # # # # # #
    #
    #  obterPino
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def obterPino(self, msg):
        pino = -1
        while not pino in range(4):
            try:
                pino = int(input(msg))
            except:
                print("Deve ser um valor numérico")
                input("<Enter>")
        return pino


    # # # # # # # # # # # # # # # # # # # # # #
    #
    #  isGameOver
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def isGameOver(self):
        return self.gameOver


    # # # # # # # # # # # # # # # # # # # # # #
    #
    #  recuperarGame
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def recuperarGame(self):
        if not exists(self.nomeArquivo):
            return False

        if not self.obterRespostaSN("Existe um game salvo. Quer carregar este jogo? (s/n) "):
            return False

        try:
            with open(self.nomeArquivo) as f:
                data = json.load(f)
            self.numDiscos = int(data["numDiscos"])
            self.numMovimentos = int(data["numMovimentos"])
            self.inicializaPinosDiscos()
            for valor in data["p1"]:
                aux = valor//2
                if aux > 0:
                    self.pinos[0].empilharDisco(self.discos[aux-1])
            for valor in data["p2"]:
                aux = valor//2
                if aux > 0:
                    self.pinos[1].empilharDisco(self.discos[aux-1])
            for valor in data["p3"]:
                aux = valor//2
                if aux > 0:
                    self.pinos[2].empilharDisco(self.discos[aux-1])
        except:
            print("Algo deu errado ao carregar o game...")
            input("<Enter>")
        return True


    # # # # # # # # # # # # # # # # # # # # # #
    #
    #  salvarGame
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def salvarGame(self):
        if not self.obterRespostaSN("Game finalizado. Quer salvar este jogo? (s/n) "):
            return False

        try:
            myDict = {
                "numDiscos" : self.numDiscos,
                "numMovimentos" : self.numMovimentos
            }
            myDict.update({"p1" : self.pinos[0].toList()})
            myDict.update({"p2" : self.pinos[1].toList()})
            myDict.update({"p3" : self.pinos[2].toList()})

            with open(self.nomeArquivo, "w") as file:
                json.dump(myDict, file)
        except:
            print("Algo deu errado ao salvar o game...")
            input("<Enter>")


    # # # # # # # # # # # # # # # # # # # # # #
    #
    #  movimentarDisco
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def movimentarDisco(self):
        self.imp.clear()
        self.imp.mostrar(self.pinos)
        print("Movimentos executados: "+str(self.numMovimentos))

        origem = self.obterPino("Retirar disco de qual pino (1 a 3, 0 = fim)? ")
        if origem == 0:
            self.gameOver = True
            self.salvarGame()
            return

        destino = self.obterPino("Mover disco para qual pino (1 a 3, 0 = fim)? ")
        if destino == 0:
            self.gameOver = True
            self.salvarGame()
            return

        if self.pinos[origem-1].isVazio():
            print("Este pino está vazio")
            input("<Enter>")
            return

        origem -= 1
        destino -= 1
        discoOrigem = self.pinos[origem].topo()
        discoDestino = self.pinos[destino].topo()
        if discoDestino != None:
            if discoOrigem.tamanho > discoDestino.tamanho:
                print("O disco a ser movido deve ser menor que o disco no topo do pino de destino")
                input("<Enter>")
                return

        discoMovimentado = self.pinos[origem].desempilharDisco()
        if not self.pinos[destino].empilharDisco(discoMovimentado):
            print("Houve um erro ao movimentar o disco")
            input("<Enter>")
            return

        self.numMovimentos += 1
        if self.pinos[0].isVazio() and (self.pinos[1].isVazio() or self.pinos[2].isVazio()):
            self.gameOver = True
            self.imp.clear()
            self.imp.mostrar(self.pinos)
            print(f"Muito bom, você conseguiu mover a torre de Hanoi em {self.numMovimentos} movimentos:\n")
            if self.carregouGame:
                resposta = ""
                while not resposta in ['s','n']:
                    try:
                        resposta = input("Game finalizado. Quer remover o jogo salvo? (s/n) ")
                    except:
                        print("Algo deu errado...")
                        input("<Enter>")
                if resposta == 's':
                    os.remove(self.nomeArquivo)
