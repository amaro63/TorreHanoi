from os import system
from os import name

class display:

    # # # # # # # # # # # # # # # # # # # # # #
    #
    # ctor
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self):
        self.branco = " "
        self.item = "="
        self.bottom = 75*self.item
        self.vazia = "               |                    |                    |"


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # mostrar
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def mostrar(self, pinos):
        print("\n               1                    2                    3\n")
        l = len(pinos[0].pilha)
        for i in range(l):
            print(self.vazia)
            linha = "     "
            linha += self.formata_disco(pinos[0].pilha[l-i-1])
            linha += self.formata_disco(pinos[1].pilha[l-i-1])
            linha += self.formata_disco(pinos[2].pilha[l-i-1])
            print(linha)
        print(self.vazia)
        print(self.bottom)


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # clear
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # formata_disco
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def formata_disco(self, d):
        linha = "          |          "
        if type(d) is not int:
            sz = d.toString()
            br = (21-len(sz))//2
            linha = br*self.branco+sz+br*self.branco
        return linha
