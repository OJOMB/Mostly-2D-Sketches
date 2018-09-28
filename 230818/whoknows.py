import pygame as pg
import random
import math

width = 1200
height = 800

black = (0,0,0)
white = (255,255,255)

pg.init()
clock = pg.time.Clock()
fps = 6
screen = pg.display.set_mode([width, height])
pointlist = []
counter = 1
def r_element(r, counter):
    return (r+counter)%100 + 50

def g_element(g, counter):
    if counter % 255 != 0:
        return g % (counter % 255)
    else:
        return g + 1

def b_element(b, counter):
    return abs(r - counter) % 100 + 50

r = 255
g = 255
b = 0
while True:
    clock.tick(fps)
    screen.fill((r, g, b))
    r = r_element(r, counter)
    g = g_element(g, counter)
    b = b_element(b, counter)
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
    for x in range(0, width):
        y = int(math.sinh((x + counter) * 0.05) * (math.sin(counter)*200) + height/2)
        pointlist.append([x,y])
    r1 = r + 20 if r <= 235 else r - 255 + 20
    g1 = g + 20 if g <= 235 else g - 255 + 20
    b1 = b + 20 if b <= 235 else b - 255 + 20
    pg.draw.lines(screen, (r1,g1,b1), False, pointlist, 3)
    pg.display.flip()
    pointlist = []
    counter += 1

