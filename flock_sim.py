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
boids = 20
boids_pos = []
unit_vectors = []
vector_mag = 10
velocity = []
for i in range(boids):
    velocity.append(random.uniform(0.00001, 0.004))

def vector(x,y):
    magnitude = math.sqrt((x*x)+(y*y))
    x = x/magnitude
    y = y/magnitude
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

def flock_loop():
    global run
    global boids
    time1 = time.time()
    vector_adj()
    while run:
        update()
        time2 = time.time()
        if (time2 - time1)>=wait_time:
            render()
            time1 = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
flock_loop()