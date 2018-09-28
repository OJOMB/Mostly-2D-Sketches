import pygame as pg
import random
import math

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

all_sprites = pg.sprite.Group()
col_count = 0
#top right balls
for i in range(0,361, 30):
    circle = CircularMotion([897, 260], juice_zone[col_count%5], 90, 10, 16, i)
    all_sprites.add(circle)
    col_count += 1

col_count = 0
#bottom right balls
for i in range(0,361, 30):
    circle = CircularMotion([897, 520], juice_zone[col_count%5], 
                            90, 10, 16, i, clockwise=False)
    all_sprites.add(circle)
    col_count += 1

col_count = 0
#top left balls
for i in range(0,361, 30):
    circle = CircularMotion([299, 260], juice_zone[col_count%5],
                            90, 10, 16, i, clockwise=False)
    all_sprites.add(circle)
    col_count += 1

col_count = 0
#bottom left balls
for i in range(0,361, 30):
    circle = CircularMotion([299, 520], juice_zone[col_count%5], 90, 10, 16, i)
    all_sprites.add(circle)
    col_count += 1

rectlist = []
x = width/2
y = 0
h = 10
w = [int(3*1.8**i) for i in range(10)] + [int(3*1.8**i) for i in range(9,-1,-1)]

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

y = 260

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

y = 520

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

x = width
y = 0

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

y = 260

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

y = 520

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

x = 0
y = 0

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

y = 260

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

y = 520

for i in range(len(w)):
    box = pg.Rect([0,0,w[i],h])
    box.centerx = x
    box.top = y
    rectlist.append(box)
    y += h + 3

small_radii = [i for i in range(1,30)] + [i for i in range(30,0,-1)]
front_radii = [i for i in range(9,75,3)] + [i for i in range(75,8,-3)]
back_radii = [i for i in range(75,8,-3)] + [i for i in range(9,75,3)]

grid_start = []
grid_stop = []

for i in range(0,1197,4):
    grid_start.append([i,0])
    grid_stop.append([i,780])

counter = 0
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

    #draw red horizontal lines on top of black fill
    for start_pos, end_pos in zip(grid_start,grid_stop):
        pg.draw.line(screen, red, start_pos, end_pos)

    #draw four coloured rects behind box pattern 
    pg.draw.rect(screen, edgy_watermelon[0], [0,127,width/2,254])
    pg.draw.rect(screen, edgy_watermelon[1], [width/2,127,596,254])
    pg.draw.rect(screen, edgy_watermelon[2], [0,height/2,596,254])
    pg.draw.rect(screen, edgy_watermelon[3], [width/2,height/2,596,254])

    #draw symmetrical box pattern 
    for box in rectlist:
        pg.draw.rect(screen, juice_zone[counter%len(juice_zone)], box)
        counter += 1

    #draw triangles to frame centrepiece
    #top left
    pg.draw.polygon(screen, black, [[165, 117], [299, 0], [431, 117]])
    #bottom left
    pg.draw.polygon(screen, black, [[165, 660], [299, height], [431, 660]])
    #top right
    pg.draw.polygon(screen, black, [[761, 117], [895, 0], [1027, 117]])
    #bottom right
    pg.draw.polygon(screen, black, [[761, 660], [895, height], [1027, 660]])   


    #draw circles on top of four coloured rects
    pg.draw.circle(screen, white, [897, 260], 100)
    pg.draw.circle(screen, juice_zone[counter%len(juice_zone)], [897, 260], back_radii[counter%len(back_radii)])
    pg.draw.circle(screen, edgy_watermelon[counter%len(edgy_watermelon)], [897, 260], front_radii[counter%len(front_radii)])
    pg.draw.circle(screen, black, [897, 260], small_radii[counter%len(small_radii)])
    pg.draw.circle(screen, white, [897, 520], 100)
    pg.draw.circle(screen, juice_zone[counter%len(juice_zone)], [897, 520], back_radii[counter%len(back_radii)])
    pg.draw.circle(screen, edgy_watermelon[counter%len(edgy_watermelon)], [897, 520], front_radii[counter%len(front_radii)])
    pg.draw.circle(screen, black, [897, 520], small_radii[counter%len(small_radii)])
    pg.draw.circle(screen, white, [299, 260], 100)
    pg.draw.circle(screen, juice_zone[counter%len(juice_zone)], [299, 260], back_radii[counter%len(back_radii)])
    pg.draw.circle(screen, edgy_watermelon[counter%len(edgy_watermelon)], [299, 260], front_radii[counter%len(front_radii)])
    pg.draw.circle(screen, black, [299, 260], small_radii[counter%len(small_radii)])
    pg.draw.circle(screen, white, [299, 520], 100)
    pg.draw.circle(screen, juice_zone[counter%len(juice_zone)], [299, 520], back_radii[counter%len(back_radii)])
    pg.draw.circle(screen, edgy_watermelon[counter%len(edgy_watermelon)], [299, 520], front_radii[counter%len(front_radii)])
    pg.draw.circle(screen, black, [299, 520], small_radii[counter%len(small_radii)])
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()

    counter += 1

