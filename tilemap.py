import pygame as pg
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Map(object):
    #creats multiple maps, and assigns new variable used by the "camera"
     def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())#strip takes away characters such as \n when reading it

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera(object):
    # creates a "camera to follow play by off setting the drawing of the screen
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # tracks an entity
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        #updates the "camera" to shift the drawing appropriately
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        #limit scrolling to map size
        x = min(0, x)#left side
        y = min(0, y)#top
        x = max(-(self.width - WIDTH), x)#right side
        y = max(-(self.height - HEIGHT),y)#bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
