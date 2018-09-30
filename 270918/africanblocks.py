import pygame as pg
import random
import math

width = 1400
height = 888

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
maverick = [(248,10,0), (248,10,0), (236,198,0), (36,75,28), (23,34,67)]
pastelfish = [(225,205,102), (102,102,102), (229,90,118), (212,172,178), (198,184,206)]

def diamond_blocks(surface, fill_col, border_col, 
                   width, height, no_of_blocks, centrepoint):
    #middle block accounting for indexing from 0
    middle_block = (no_of_blocks - 1 ) / 2
    #individual block width
    w = int(width / middle_block + 1)    
    #individual block height
    h = int(height/no_of_blocks)
    x = centrepoint[0] - int(w/2)
    y = centrepoint[1] - int(height/2) - int(h/2)
    for i in range(no_of_blocks):
        if i == 0:
            pg.draw.rect(surface, border_col, [x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [x+2,y+2,w-4,h-4])
            r_x = x + int(w/2)
            l_x = x - int(w/2)
            y += h
        elif 0 < i < middle_block:
            pg.draw.rect(surface, border_col, [r_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [r_x+2,y+2,w-4,h-4])
            pg.draw.rect(surface, border_col, [l_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [l_x+2,y+2,w-4,h-4])
            r_x += int(w/2)
            l_x -= int(w/2)
            y += h
        elif middle_block <= i < no_of_blocks-1:
            pg.draw.rect(surface, border_col, [r_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [r_x+2,y+2,w-4,h-4])
            pg.draw.rect(surface, border_col, [l_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [l_x+2,y+2,w-4,h-4])
            r_x -= int(w/2)
            l_x += int(w/2)
            y += h
        elif i == no_of_blocks-1:
            pg.draw.rect(surface, border_col, [r_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [r_x+2,y+2,w-4,h-4], 2)

def stacked_triangle(surface, position):
    w = 135
    h = 10
    x = position[0]
    y = position[1]
    col_count = 3
    for i in range(0, 6):
        if i != 4:
            pg.draw.rect(surface, maverick[col_count], [x,y,w,h])
            pg.draw.rect(surface, maverick[1], [x,y,w,h], 3)
            w -= 26
            y += 11
            x += 13
            col_count += 1
            if col_count >=5:
                col_count = 3
        else:
            pg.draw.rect(surface, maverick[col_count], [x,y,w,h])
            pg.draw.rect(surface, maverick[1], [x,y,w,h], 3)
            w -= 20
            y += 11
            x += 10
            col_count += 1
            if col_count >=5:
                col_count = 3

def static_diamond_blocks(surface, fill_col, border_col, no_of_blocks, 
                          centrepoint):
    #middle block accounting for indexing from 0
    middle_block = (no_of_blocks - 1 ) / 2
    #individual block width
    w = 20    
    #individual block height
    h = 10
    x = centrepoint[0] - int(w/2)
    y = centrepoint[1] - int(h*no_of_blocks/2) - int(h/2)
    for i in range(no_of_blocks):
        if i == 0:
            pg.draw.rect(surface, border_col, [x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [x+2,y+2,w-3,h-3])
            r_x = x + int(w/2)
            l_x = x - int(w/2)
            y += h
        elif 0 < i < middle_block:
            pg.draw.rect(surface, border_col, [r_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [r_x+2,y+2,w-3,h-3])
            pg.draw.rect(surface, border_col, [l_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [l_x+2,y+2,w-3,h-3])
            r_x += int(w/2)
            l_x -= int(w/2)
            y += h
        elif middle_block <= i < no_of_blocks-1:
            pg.draw.rect(surface, border_col, [r_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [r_x+2,y+2,w-3,h-3])
            pg.draw.rect(surface, border_col, [l_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [l_x+2,y+2,w-3,h-3])
            r_x -= int(w/2)
            l_x += int(w/2)
            y += h
        elif i == no_of_blocks-1:
            pg.draw.rect(surface, border_col, [r_x,y,w,h], 2)
            pg.draw.rect(surface, fill_col, [r_x+2,y+2,w-3,h-3])

class MovingTriangle(pg.sprite.Sprite):
    def __init__(self, x, y, flipped=False, leftwards=False):
        super().__init__()
        self.image = pg.Surface((140,65))
        self.image.set_colorkey(black)
        stacked_triangle(self.image, [0,0])
        if flipped:
            self.image = pg.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.leftwards = leftwards
        if leftwards:
            self.speedx = -30
        else:
            self.speedx = 30

    def update(self):
        self.rect.x += self.speedx
        if self.leftwards:
            if self.rect.right < 0:
                self.rect.left = width
        else:
            if self.rect.left > width:
                self.rect.right = 0

pg.init()
clock = pg.time.Clock()
fps = 7
screen = pg.display.set_mode([width, height])

height_list = [i for i in range(99,800,3)] + [i for i in range(799,99,-3)]

all_sprites = pg.sprite.Group()
flipped = 0
for x_coord in range(0, 1401, 140):
    triangle = MovingTriangle(x_coord, 249, flipped=flipped)
    all_sprites.add(triangle)
    if flipped:
        flipped = False
    else:
        flipped = True

flipped = 0
for x_coord in range(0, 1401, 140):
    triangle = MovingTriangle(x_coord, 568, flipped=flipped, leftwards=True)
    all_sprites.add(triangle)
    if flipped:
        flipped = False
    else:
        flipped = True

counter = 0
while True:
    screen.fill(white)
    for i in range(0, 1401, 20):
        pg.draw.line(screen, maverick[4], [i, 0], [i,height])
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
    #1st bars
    bar_col = 1
    for x_coord in range (0, 1261, 140):
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 0, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 0, 135, 10], 3)
        bar_col +=1
        if bar_col >= 3:
            bar_col = 1
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 13, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 13, 135, 10], 3)

    #top diamonds
    for x_coord in range(100, 1301, 200):
        for i in range(19, 2, -4):
            if i == 19:
                static_diamond_blocks(screen, black, black, i,[x_coord,126])
            else:
                static_diamond_blocks(screen, maverick[counter%5], black, i,[x_coord,126])
                counter+=1

    #2nd bars
    bar_col = 2
    for x_coord in range (0, 1261, 140):
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 220, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 220, 135, 10], 3)
        bar_col +=1
        if bar_col >= 3:
            bar_col = 1
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 233, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 233, 135, 10], 3)
    
    #triangles appear next

    #3rd bars
    bar_col = 1
    for x_coord in range (0, 1261, 140):
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 321, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 321, 135, 10], 3)
        bar_col +=1
        if bar_col >= 3:
            bar_col = 1
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 334, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 334, 135, 10], 3)

    #mid diamonds
    for x_coord in range(100, 1301, 200):
        for i in range(19, 2, -4):
            if i == 19:
                static_diamond_blocks(screen, black, black, i,[x_coord,447])
            else:
                static_diamond_blocks(screen, pastelfish[counter%5], black, i,[x_coord,447])
                counter+=1

    #4th bars
    bar_col = 2
    for x_coord in range (0, 1261, 140):
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 541, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 541, 135, 10], 3)
        bar_col +=1
        if bar_col >= 3:
            bar_col = 1
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 554, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 554, 135, 10], 3)

    #triangles appear next

    #5th bars
    bar_col = 1
    for x_coord in range (0, 1261, 140):
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 638, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 638, 135, 10], 3)
        bar_col +=1
        if bar_col >= 3:
            bar_col = 1
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 651, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 651, 135, 10], 3)

    #bottom diamonds
    for x_coord in range(100, 1301, 200):
        for i in range(19, 2, -4):
            if i == 19:
                static_diamond_blocks(screen, black, black, i,[x_coord,764])
            else:
                static_diamond_blocks(screen, maverick[counter%5], black, i,[x_coord,764])
                counter+=1
    #6th bars
    bar_col = 2
    for x_coord in range (0, 1261, 140):
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 864, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 864, 135, 10], 3)
        bar_col +=1
        if bar_col >= 3:
            bar_col = 1
        pg.draw.rect(screen, maverick[bar_col], [x_coord, 877, 135, 10])
        pg.draw.rect(screen, black, [x_coord, 877, 135, 10], 3)

    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
