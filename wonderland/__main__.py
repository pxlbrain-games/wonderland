import arcade

from wonderland.game import Wonderland

SCREEN_WIDTH = 1248
SCREEN_HEIGHT = 702

game = Wonderland(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup()
arcade.run()
