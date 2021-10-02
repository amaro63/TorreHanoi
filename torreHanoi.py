from manager import manager

gameManager = manager(3, 7)
gameManager.inicializar()
while not gameManager.isGameOver():
    gameManager.movimentarDisco()
