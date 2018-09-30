import pygame as pg
import random
import math
import time

width = 1196
height = 780

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
juice_zone = [(242,175,92), (238,137,93), (214,96,75), (174,71,66), (144,51,51)]
edgy_watermelon = [(133,48,55),(255,61,78),(210,95,108),(20,61,29),(56,122,74)]

pg.init()
clock = pg.time.Clock()
fps = 15
screen = pg.display.set_mode([width, height])

class CircularMotion(pg.sprite.Sprite):
    def __init__(self, centre_pos, colour, radius, speed, diameter, angle, clockwise=True):
        super().__init__()
        self.image = pg.Surface([int(diameter), int(diameter)])
        self.image.set_colorkey(black)
        pg.draw.circle(self.image, colour, [int(diameter/2),int(diameter/2)], int(diameter/2))
        self.rect = self.image.get_rect()
        self.centre_pos = centre_pos
        self.rad = radius
        self.rect.centerx = centre_pos[0]
        self.rect.centery = centre_pos[1]
        self.speed = speed
        self.angle = angle
        self.clockwise = clockwise

    def update(self):
        if self.clockwise:
            self.angle = (self.angle + self.speed) % 360
        else:
            self.angle = (self.angle - self.speed) % 360
        y = self.rad*math.sin(math.radians(self.angle))
        self.rect.centery = self.centre_pos[1] + y
        x = self.rad*math.cos(math.radians(self.angle))
        self.rect.centerx = self.centre_pos[0] + x

circle = CircularMotion([width/2,height/2], 300, 6, 60, 0)
all_sprites = pg.sprite.Group()
all_sprites.add(circle)

while True:
    screen.fill(black)
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = True
                while pause:
                    for event in pg.event.get():
                          if event.type == pg.QUIT:
                            pg.quit()
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_SPACE:
                                    pause = False
    all_sprites.update()
    all_sprites.draw(screen)
    pg.draw.rect(screen, white, [width/2,height/2,5,5])
    pg.draw.line(screen, white, [width/2,height/2], [circle.rect.centerx,circle.rect.centery])
    pg.display.flip()
