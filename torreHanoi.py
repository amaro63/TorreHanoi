from manager import manager

gameManager = manager(3, 7)
while not gameManager.isGameOver():
    gameManager.movimentarDisco()
