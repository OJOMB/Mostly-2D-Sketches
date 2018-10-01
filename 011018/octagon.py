import pygame as pg
import random
import math

width = 1200
height = 800

white = (255,255,255)
black = (0,0,0)

dawns = [(245,0,87), (158,87,159), (72,192,114), (255,162,181), (245,253,149)]

pg.init()
clock = pg.time.Clock()
fps = 20
screen = pg.display.set_mode([width, height])



def octagon_vertices_plotter(x,y,radius):
    oct_vertices = []
    for i in range(8):
        oct_vertices.append(
            (
                x + 100 * math.cos(((2*math.pi)/8)*i),
                y + 100 * math.sin(((2*math.pi)/8)*i)               
            )
        )
    return oct_vertices

vertices = []

for x in range(0, 1201, 200):
    for y in range(0,801,200):
        vertices.append(octagon_vertices_plotter(x, y, 100))

fill_count = 0
counter = 0
while True:
    clock.tick(fps)
    screen.fill(dawns[fill_count])
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

    vertices = []

    radius = (counter) + 25

    for x in range(0, 1201, 2*radius):
        for y in range(0,801,2*radius):
            vertices.append(octagon_vertices_plotter(x, y, radius))

    for octagon in vertices:
        pg.draw.polygon(screen, dawns[counter % 5], octagon, 5)
                         
    pg.display.flip()
    counter +=1
    counter %= 100
    if counter == 99:
        fill_count += 1
        fill_count %= 5
