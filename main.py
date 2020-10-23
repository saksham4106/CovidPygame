from gameClass import *

g = Game()
g.startScreen()
while g.running:
    g.new()
    g.gameOverScreen()
