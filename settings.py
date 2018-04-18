#########################################
#
#                   settings
#
#########################################
import pygame as pg
vec = pg.math.Vector2


# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 800
HEIGHT = 400
FPS = 60
TITLE = "The Dungeon"
BGCOLOR = BROWN

TILESIZE = 20
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = "brick_brown-vines_1.png"

#play settings
PLAYER_SPEED = 175
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BOW_OFFSET = vec(30, 10)

#weapon settings
ARROW_IMG = "Arrow.png"
ARROW_SPEED = 500
ARROW_RATE = 250

#mob settings
MOB_IMG = "robot1_hold.png"
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 35, 35)
