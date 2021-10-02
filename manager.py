from disco import disco
from pino import pino
from display import display
from os import system, name


class manager:

    def __init__(self, min, max):
        self.numDiscos = self.obterNumeroDiscos(min, max)
        self.p1 = pino(self.numDiscos)
        self.p2 = pino(self.numDiscos)
        self.p3 = pino(self.numDiscos)
        self.pinos = [self.p1, self.p2, self.p3]
        self.discos = []
        for i in range(self.numDiscos):
            self.discos.append(disco(1+2*(i+1)))
        self.imp = display()
        self.gameOver = False

    def inicializar(self):
        for i in range(self.numDiscos):
            self.p1.empilharDisco(self.discos[self.numDiscos-1-i])

    def obterNumeroDiscos(self, min, max):
        self.clear()
        discos = 0
        while not discos in range(min, max+1):
            try:
                discos = int(input("Quantos discos ("+str(min) + " a "+str(max) + ")? "))
            except:
                print("Valor inválido.")
        return discos

    def obterPino(self, msg):
        pino = -1
        while not pino in range(4):
            try:
                pino = int(input(msg))
            except:
                print("Deve ser um valor numérico")
                input("<Enter>")
        return pino

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def isGameOver(self):
        return self.gameOver

    def movimentarDisco(self):
        self.clear()
        self.imp.mostrar(self.pinos)
        origem = self.obterPino("Retirar disco de qual pino (1 a 3, 0 = fim)? ")
        if origem == 0:
            self.gameOver = True
            return
        destino = self.obterPino("Mover disco para qual pino (1 a 3, 0 = fim)? ")
        if destino == 0:
            self.gameOver = True
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
        if self.pinos[0].isVazio() and (self.pinos[1].isVazio() or self.pinos[2].isVazio()):
            self.gameOver = True
            self.clear()
            self.imp.mostrar(self.pinos)
            print("Muito bom, você conseguiu mover a torre de Hanoi\n")
        return
