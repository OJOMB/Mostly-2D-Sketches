import pygame as pg
import random
import math

width = 1440
height = 800

black = (0,0,0)
white = (255,255,255)
edgy_watermelon = [(255,255,255),(133,48,55),(255,61,78),(210,95,108),(20,61,29),(56,122,74)]
juice_zone = [(242,175,92), (238,137,93), (214,96,75), (174,71,66), (144,51,51)]

pg.init()
clock = pg.time.Clock()
fps = 100
screen = pg.display.set_mode([width, height])

def round(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0 

class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, radius, palette, r2l=True):
        super().__init__()
        self.palette = palette
        self.rad = radius
        self.r2l = r2l
        self.image = pg.Surface([self.rad*2, self.rad*2])
        pg.draw.circle(self.image, palette[0], [self.rad,self.rad], self.rad)
        pg.draw.circle(self.image, palette[1], [self.rad,self.rad], int(self.rad*0.66))
        pg.draw.circle(self.image, palette[2], [self.rad,self.rad], int(self.rad*0.33))
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.y = y
        self.rect.centery = y
        self.speedx = 3

    def change_colour(self):
        pass

    def update(self):
        if self.r2l:
            self.rect.right += self.speedx
            if self.rect.left > width:
                self.rect.right = 0
                self.rect.centery = self.y
                pg.draw.circle(self.image, random.choice(self.palette), [self.rad,self.rad], self.rad)
                pg.draw.circle(self.image, random.choice(self.palette), [self.rad,self.rad], int(self.rad*0.66))
                pg.draw.circle(self.image, random.choice(self.palette), [self.rad,self.rad], int(self.rad*0.33))
            self.rect.y += round((math.sin(math.radians(abs(self.rect.right%360)*2))))
        else:
            self.rect.right -= self.speedx
            if self.rect.right < 0:
                self.rect.left = width
                self.rect.centery = self.y
                pg.draw.circle(self.image, random.choice(self.palette), [self.rad,self.rad], self.rad)
                pg.draw.circle(self.image, random.choice(self.palette), [self.rad,self.rad], int(self.rad*0.66))
                pg.draw.circle(self.image, random.choice(self.palette), [self.rad,self.rad], int(self.rad*0.33))
            self.rect.y += round((math.sin(math.radians(abs(self.rect.right%360)*2))))

all_sprites = pg.sprite.Group()

x = -50
y = height/5
radius = 30
for i in range(6):
    circle = Circle(x,y * i,radius, edgy_watermelon)
    all_sprites.add(circle)
    x -= 100

x = width + 50
y = (height)/5
radius = 30
for i in range(6):
    circle = Circle(x,y * i,radius, edgy_watermelon, r2l=False)
    all_sprites.add(circle)
    x += 100

x = -100
y = 80
radius = 15
for i in range(3):
    circle = Circle(x,y,radius, juice_zone)
    all_sprites.add(circle)
    x += 100
    y += 320

x = width + 100
y = 80
radius = 15
for i in range(3):
    circle = Circle(x,y,radius, juice_zone, r2l=False)
    all_sprites.add(circle)
    x -= 100
    y += 320



screen.fill((black))
while True:
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
                        if event.type == pg.KEYUP:
                            if event.key == pg.K_SPACE:
                                pause = False
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()

