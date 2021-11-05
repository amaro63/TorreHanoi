class disco:

    # # # # # # # # # # # # # # # # # # # # # #
    #
    # ctor
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, tamanho):
        self.tamanho = tamanho


    # # # # # # # # # # # # # # # # # # # # # #
    #
    # toString
    #
    # # # # # # # # # # # # # # # # # # # # # #
    def toString(self):
        pad = self.tamanho//2
        if pad == 1:
            return ("<" + str(pad) + ">")
        else:
            return ((pad-1)*"<" + "-" + str(pad) + "-" + (pad-1)*">")
