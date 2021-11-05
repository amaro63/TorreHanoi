from disco import disco
import json

class pino:

    # # # # # # # # # # # # # # # # # # # # # #
    #
    # ctor
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, numPosicoes):
        self.numPosicoes = numPosicoes
        self.proximoVazio = 0
        self.pilha = []
        for i in range(numPosicoes):
            self.pilha.append(0)


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # toList
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def toList(self):
        jsonList = []
        for item in self.pilha:
            if type(item) is disco:
                jsonList.append(item.tamanho)
            else:
                jsonList.append(0)
        return jsonList


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # isCheio
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def isCheio(self):
        return (self.proximoVazio == -1)


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # isVazio
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def isVazio(self):
        return (self.proximoVazio == 0)


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # empilharDisco
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def empilharDisco(self, disco):
        if self.isCheio():
            return False
        if not self.isVazio():
            if disco.tamanho > self.pilha[self.proximoVazio-1].tamanho:
                return False
        self.pilha[self.proximoVazio] = disco
        if self.proximoVazio == len(self.pilha)-1:
            self.proximoVazio = -1
        else:
            self.proximoVazio += 1
        return True


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # obterIndiceTopo
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def obterIndiceTopo(self):
        if self.isVazio():
            return None
        if self.isCheio():
            indice = len(self.pilha)-1
        else:
            if self.proximoVazio > 0:
                indice = self.proximoVazio-1
            else:
                indice = 0
        return indice


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # desempilharDisco
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def desempilharDisco(self):
        indice = self.obterIndiceTopo()
        if indice == None:
            return None
        disco = self.pilha[indice]
        self.pilha[indice] = 0
        self.proximoVazio = indice
        return disco


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # topo
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def topo(self):
        indice = self.obterIndiceTopo()
        if indice == None:
            return None
        return self.pilha[indice]
