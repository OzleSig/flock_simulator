import pygame
from pygame.locals import *
pygame.init()
import time
import math
import random

windowsize = 800
white = (255,255,255)
black = (0,0,0)
surface = pygame.display.set_mode((windowsize,windowsize))
run = True
wait_time = 1/60 #in seconds
boids = 10
boids_pos = []
unit_vectors = []
vector_mag = 20
velocity = []
for i in range(boids):
    velocity.append(random.uniform(0.001, 0.004))
visibility = 50
align_fac = 0.3

def vector(x,y):
    magnitude = math.sqrt((x*x)+(y*y))
    x = x/magnitude
    y = y/magnitude
    print(magnitude)
    return [x,y]

def vector_adj():
    global boids_pos
    for i in range(boids):
        boids_pos.append([random.randint(-windowsize, windowsize), random.randint(-windowsize, windowsize)])
        x = boids_pos[i][0]
        y = boids_pos[i][1]
        boids_pos[i] = vector(x,y)
        unit_vectors.append(boids_pos[i])
        x_adj = random.randint(0, windowsize)
        y_adj = random.randint(0, windowsize)
        x = x_adj + boids_pos[i][0]*vector_mag
        y = y_adj + boids_pos[i][1]*vector_mag
        boids_pos[i] = [x,y]

def render():
    surface.fill(white)
    draw_boid()
    pygame.display.flip()

def update():
    for i, coord in enumerate(boids_pos):
        coord[0] = coord[0] % windowsize
        coord[1] = coord[1] % windowsize
        coord[0]+= unit_vectors[i][0]*velocity[i]
        coord[1]+= unit_vectors[i][1]*velocity[i]
                

def draw_boid():
    for i, coord in enumerate(boids_pos):
        x = coord[0]
        y = coord[1]
        x_adj = x + unit_vectors[i][0]*vector_mag
        y_adj = y + unit_vectors[i][1]*vector_mag
        pygame.draw.line(surface, black, (x_adj,y_adj), (x,y))

def visable_range():
    for n1, main in enumerate(boids_pos):
        x1 = main[0]
        y1 = main[1]
        for n2, neighbour in enumerate(boids_pos): 
            x2 = neighbour[0]
            y2 = neighbour[1]
            
#def in_vis_range (point1, point2):
#    for points in point1:

#    return math.sqrt(abs(x1-x2))**2 + math.sqrt(abs(y1-y2))**2 < math.sqrt(visibility**2)

#boids_pos[n1] = [(x1-x2)/2 + x1, (y1-y2)/2 + y1]
#boids_pos[n2] = [(x1-x2)/2 + x2, (y1-y2)/2 + y2]

def flock_loop():
    global run
    global boids
    time1 = time.time()
    vector_adj()
    while run:
        update()
        visable_range()
        time2 = time.time()
        if (time2 - time1)>=wait_time:
            render()
            time1 = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
flock_loop()