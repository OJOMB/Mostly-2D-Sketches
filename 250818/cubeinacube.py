import pygame
from pygame.locals import *
import random
from OpenGL.GL import *
from OpenGL.GLU import *

"""
There is no point in hardcoding vertices/edges, it's done for no reason.
The methods to generate vertices/edges are included further down in the 
AutoCube class
"""

number_of_cubes = 5

vertices = (
    #INNERMOST CUBE
    #---front face = (0-3)---
    (0,0,0), (1,0,0), (1,1,0), (0,1,0),
    #---back face = (4-7)---
    (0,0,1), (1,0,1), (1,1,1), (0,1,1),
    #OUTER CUBE
    #---front face = (8-11)---
    (-1,-1,-1), (2,-1,-1), (2,2,-1), (-1,2,-1),
    #---back face = (12-15)---
    (-1,-1,2), (2,-1,2), (2,2,2), (-1,2,2),
    #OUTER**2 CUBE
    #---front face = (16-19)---
    (-2,-2,-2), (3,-2,-2), (3,3,-2), (-2,3,-2),
    #---back face = (20-23)---
    (-2,-2,3), (3,-2,3), (3,3,3), (-2,3,3),
    #OUTER**3 CUBE
    #---front face = (24-27)---
    (-3,-3,-3), (4,-3,-3), (4,4,-3), (-3,4,-3),
    #---back face = (28-31)---
    (-3,-3,4), (4,-3,4), (4,4,4), (-3,4,4),
    #OUTER**4 CUBE
    #---front face = (32-35)---
    (-4,-4,-4), (5,-4,-4), (5,5,-4), (-4,5,-4),
    #---back face = (36-39)---
    (-4,-4,5), (5,-4,5), (5,5,5), (-4,5,5)


)

edges = (
    (0,1), (0,3), (0,4), (0,8),
    (1,5), (1,2), (1,9), 
    (2,6), (2,3), (2,10),
    (3,7), (3,11),
    (4,5), (4,7), (4,12),
    (5,6), (5,13),
    (6,7), (6,14),
    (7,15),
    (8,9), (8,11), (8,12), (8,16),
    (9,10), (9,13), (9,17),
    (10,11), (10,14), (10,18),
    (11,15), (11,19),
    (12,13), (12,15), (12,20),
    (13,14), (13,21),
    (14,15), (14,22),
    (15,23),
    (16,17), (16,19), (16,20), (16,24),
    (17,18), (17,21), (17,25),
    (18,19), (18,22), (18,26),
    (19,23), (19,27),
    (20,21), (20,23), (20,28),
    (21,22), (21,29),
    (22,23), (22,30),
    (23,31),
    (24,25), (24,27), (24,28), (24,32),
    (25,26), (25,29), (25,33),
    (26,27), (26,30), (26,34),
    (27,31), (27,35),
    (28,29), (28,31), (28,36),
    (29,30), (29,37),
    (30,31), (30,38),
    (31,39),
    (32,33), (32,35), (32,36),
    (33,34), (33,37),
    (34,35), (34,38),
    (35,39),
    (36,37), (36,39),
    (37,38),
    (38,39)

)

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def coloredcube():
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            colour = tuple([random.random()]*3)
            glColor3fv(colour)
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def surfaces_generator(n):
    inner_cube = (
        (0,1,2,3),
        (2,3,6,7),
        (4,5,6,7),
        (0,1,4,5),
        (1,2,5,7),
        (0,3,4,6),
    )

    surfaces = []

    for i in range(0,n):
        for face in inner_cube:
            surfaces.append(tuple([vertex+8*i for vertex in face]))
    
    return tuple(surfaces)

faces = surfaces_generator(number_of_cubes)

class AutoCube(object):
    def __init__(self):
        self.cubeception_lvl = 1
        self.vertices = self.vertices_generator()
        self.edges = self.edges_generator()
        self.surfaces = self.surfaces_generator()
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        self.zoom = -10

    def vertices_generator(self):
        innercube = ( 
            (0,0,0), (1,0,0), (1,1,0), (0,1,0),
            (0,0,1), (1,0,1), (1,1,1), (0,1,1)
        )

        vertices = []

        counter = 0
        for i in range(0,self.cubeception_lvl):
            for coords in innercube:
                if counter == 0:
                    vertices.append(tuple([coords[0]-1*i]*3))
                elif counter == 1:
                    vertices.append((coords[0]+(1*i),
                                    coords[1]-(1*i),
                                    coords[2]-1*i))
                elif counter == 2:
                    vertices.append((coords[0]+1*i,
                                    coords[1]+1*i,
                                    coords[2]-1*i))      
                elif counter == 3:
                    vertices.append((coords[0]-1*i,
                                    coords[1]+1*i,
                                    coords[2]-1*i))
                elif counter == 4:
                    vertices.append((coords[0]-1*i,
                                    coords[1]-1*i,
                                    coords[2]+1*i))
                elif counter == 5:
                    vertices.append((coords[0]+1*i,
                                    coords[1]-1*i,
                                    coords[2]+1*i))
                elif counter == 6:
                    vertices.append((coords[0]+1*i,
                                    coords[1]+1*i,
                                    coords[2]+1*i))
                elif counter == 7:
                    vertices.append((coords[0]-1*i,
                                    coords[1]+1*i,
                                    coords[2]+1*i))
                counter +=1
                counter %= 8
        
        return tuple(vertices)

    def edges_generator(self):
        innercube_head = (
            (0,1), (0,3), (0,4), (0,8),
            (1,5), (1,2), (1,9), 
            (2,6), (2,3), (2,10),
            (3,7), (3,11),
            (4,5), (4,7), (4,12),
            (5,6), (5,13),
            (6,7), (6,14),
            (7,15)
        )
        innercube_tail = (
            (0, 1), (0, 3), (0, 4),
            (1, 2), (1, 5),
            (2, 3), (2, 6),
            (3, 7),
            (4, 5), (4, 7),
            (5, 6),
            (6, 7)
        )
        
        edges = []

        for i in range(0,self.cubeception_lvl):
            if i != self.cubeception_lvl - 1:
                for edge in innercube_head:
                    edges.append((
                        edge[0]+i*8,
                        edge[1]+i*8
                    ))
            else:
                for edge in innercube_tail:
                    edges.append((
                        edge[0]+i*8,
                        edge[1]+i*8
                    ))

        return tuple(edges)

    def surfaces_generator(self):
        inner_cube = (
            (0,1,2,3),
            (2,3,6,7),
            (4,5,6,7),
            (0,1,4,5),
            (1,2,5,7),
            (0,3,4,6),
        )

        surfaces = []

        for i in range(0,self.cubeception_lvl):
            for face in inner_cube:
                surfaces.append(tuple([vertex+8*i for vertex in face]))
        
        return tuple(surfaces)

    def update(self):
        self.cubeception_lvl += 1
        self.zoom -= 1
        self.vertices = self.vertices_generator()
        self.edges = self.edges_generator()
        self.surfaces = self.surfaces_generator()
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        #glTranslatef(0,0,self.zoom)



pygame.init()
clock = pygame.time.Clock()
fps = 15
width = 1196
height = 780
screen = pygame.display.set_mode([width, height], DOUBLEBUF | OPENGL) 

gluPerspective(45, (width/height), 0.1, 50)

glTranslatef(0,0,-20)

glRotatef(0,0,0,0)

show_original = True

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                if show_original:
                    show_original = False
                    show_coloured = True
                elif show_coloured:
                    show_coloured = False
                    show_autocube = True
                    autocube = AutoCube()
                elif show_autocube:
                    show_autocube = False
                    show_original = True
                    #glTranslatef(0,0,-20)
                    autocube = None

    glRotatef(1,3,1,0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    if show_original:
        cube()
    elif show_coloured:
        coloredcube()
    elif show_autocube:    
        autocube.update()
    pygame.display.flip()
