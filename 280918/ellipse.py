import pygame as pg
import random
import math

width = 1200
height = 800

black = (0,0,0)
white = (255,255,255)
oranges = [
    (249,156,0), 
    (255,167,20), 
    (255,202,22), 
    (255,178,27), 
    (249,115,0), 
    (255,201,102),
    (204,132,0)
    ]
pinks = [
    (252,186,203),
    (255,136,153),
    (255,119,136),
    (233,203,209),
    (255,102,119),
    (255,85,102),
    (255,68,85)
]
blues = [
    (0,100,187),
    (40,91,135),
    (0,59,111),
    (56,126,187),
    (0,32,60),
    (239,243,248),
    (178,196,223)
]
purps = [
    (255,0,69),
    (255,0,147),
    (219,0,204),
    (191,0,219),
    (171,0,255),
    (217,72,255),
    (124,0,255)
]
greens = [
    (117,137,41),
    (140,165,45),
    (136,184,50),
    (176,191,53),
    (199,208,53),
    (71,182,37),
    (208,176,45)
]
kools = [
    (255,0,0),
    (253,255,0),
    (61,251,3),
    (124,0,255),
    (0,249,255),
    (246,255,102),
    (254,103,203)
]
yellows= [
    (239,226,37),
    (239,231,119),
    (243,236,182),
    (241,238,20),
    (249,212,18),
    (253,165,0),
    (255,252,0)    
]
jamaica = [
    (0,0,0),
    (188,4,4),
    (213,217,32),
    (91,217,54),
    (30,101,52),
    (255,255,255),
    (255,90,39)
]
pheromones = [
    (68,77,71),
    (103,126,116),
    (146,164,172),
    (221,219,219),
    (255,255,255),
    (226,255,251),
    (196,255,247)

]

p_counter = 0
palette = [
    oranges, pinks, blues, 
    purps, greens, kools, 
    yellows, jamaica, pheromones
    ]

pg.init()
clock = pg.time.Clock()
fps = 60
screen = pg.display.set_mode([width, height])

listicle = [i for i in range(7,16)]
reverse_listicle = [i for i in range(16,6,-1)]
line_width = []
for i in listicle:
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
for i in reverse_listicle:
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)
    line_width.append(i)

grid_counter = 0
grid_width = [50,100,200,400,800]

lines = True
counter = 0
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
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_SPACE:
                                pause = False
            if event.key == pg.K_RETURN:
                grid_counter += 1
                grid_counter %= 5
            if event.key == pg.K_BACKSPACE:
                p_counter += 1
                p_counter %= len(palette)
            if event.key == pg.K_RSHIFT:
                if lines:
                    lines = False
                else:
                    lines = True

    #first section
    pg.draw.rect(screen, palette[p_counter][0], [0,0,1200,160])

    for i in range(0, 1401, 20):
        pg.draw.line(screen, palette[p_counter][2], [i, 0], [i,200], line_width[counter%len(line_width)])
    for i in range(0, 201, 20):
        pg.draw.line(screen, palette[p_counter][2], [0, i], [width+10,i], line_width[counter%len(line_width)])

    if lines:
        for start_x in range (-4000 + counter % 1200,2401,grid_width[grid_counter]):
            start_pos = [start_x,0]
            end_x = 100 + start_x
            end_pos = [end_x, 200]
            pg.draw.line(screen, palette[p_counter][1], start_pos, end_pos, 10)
            end_x = (200 + (1/3)*start_x)*3
            end_pos = [end_x, 200]
            pg.draw.line(screen, palette[p_counter][1], start_pos, end_pos, 10)
            end_x = (-200 + (1/2)*start_x)*2
            end_pos = [end_x, 200]
            pg.draw.line(screen, palette[p_counter][1], start_pos, end_pos, 10)

    #second section
    start_y = 160
    end_y = 320
    diplaced_start = -3920

    pg.draw.rect(screen, palette[p_counter][1], [0,160,1200,160])

    for i in range(0, 1401, 20):
        pg.draw.line(screen, palette[p_counter][3], [i, start_y], [i,end_y], line_width[counter%len(line_width)])
    for i in range(start_y, end_y + 1, 20):
        pg.draw.line(screen, palette[p_counter][3], [0, i], [width+10,i], line_width[counter%len(line_width)])

    if lines:
        for start_x in range (diplaced_start - counter % 1200,2401,grid_width[grid_counter]):
            start_pos = [start_x,start_y]
            c = start_y - (2*start_x)
            end_x = (end_y - c)/2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][2], start_pos, end_pos, 10)
            c = start_y - ((1/3)*start_x)
            end_x = (end_y - c)*3
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][2], start_pos, end_pos, 10)
            c = start_y + ((1/2)*start_x)
            end_x = (c - end_y)*2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][2], start_pos, end_pos, 10)

    #third section
    start_y += 160
    end_y += 160
    diplaced_start += 80

    pg.draw.rect(screen, palette[p_counter][2], [0,start_y,1200,160])

    for i in range(0, 1401, 20):
        pg.draw.line(screen, palette[p_counter][4], [i, start_y], [i,end_y], line_width[counter%len(line_width)])
    for i in range(start_y, end_y + 1, 20):
        pg.draw.line(screen, palette[p_counter][4], [0, i], [width+10,i], line_width[counter%len(line_width)])

    if lines:
        for start_x in range (diplaced_start + counter % 1200,2401,grid_width[grid_counter]):
            start_pos = [start_x,start_y]
            c = start_y - (2*start_x)
            end_x = (end_y - c)/2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][3], start_pos, end_pos, 10)
            c = start_y - ((1/3)*start_x)
            end_x = (end_y - c)*3
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][3], start_pos, end_pos, 10)
            c = start_y + ((1/2)*start_x)
            end_x = (c - end_y)*2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][3], start_pos, end_pos, 10)

    #fourth section
    start_y += 160
    end_y += 160
    diplaced_start += 80

    pg.draw.rect(screen, palette[p_counter][3], [0,start_y,1200,160])

    for i in range(0, 1401, 20):
        pg.draw.line(screen, palette[p_counter][5], [i, start_y], [i,end_y], line_width[counter%len(line_width)])
    for i in range(start_y, end_y + 1, 20):
        pg.draw.line(screen, palette[p_counter][5], [0, i], [width+10,i], line_width[counter%len(line_width)])

    if lines:   
        for start_x in range (diplaced_start - counter % 1200,2401,grid_width[grid_counter]):
            start_pos = [start_x,start_y]
            c = start_y - (2*start_x)
            end_x = (end_y - c)/2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][4], start_pos, end_pos, 10)
            c = start_y - ((1/3)*start_x)
            end_x = (end_y - c)*3
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][4], start_pos, end_pos, 10)
            c = start_y + ((1/2)*start_x)
            end_x = (c - end_y)*2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][4], start_pos, end_pos, 10)

    #fifth section
    start_y += 160
    end_y += 160
    diplaced_start += 80

    pg.draw.rect(screen, palette[p_counter][4], [0,start_y,1200,160])
     
    for i in range(0, 1401, 20):
        pg.draw.line(screen, palette[p_counter][6], [i, start_y], [i,end_y], line_width[counter%len(line_width)])
    for i in range(start_y, end_y + 1, 20):
        pg.draw.line(screen, palette[p_counter][6], [0, i], [width+10,i], line_width[counter%len(line_width)])

    if lines:
        for start_x in range (diplaced_start + counter % 1200,2401,grid_width[grid_counter]):
            start_pos = [start_x,start_y]
            c = start_y - (2*start_x)
            end_x = (end_y - c)/2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][5], start_pos, end_pos, 10)
            c = start_y - ((1/3)*start_x)
            end_x = (end_y - c)*3
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][5], start_pos, end_pos, 10)
            c = start_y + ((1/2)*start_x)
            end_x = (c - end_y)*2
            end_pos = [end_x, end_y]
            pg.draw.line(screen, palette[p_counter][5], start_pos, end_pos, 10)
                         
    pg.display.flip()
    counter +=1
