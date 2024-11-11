import pygame
from pygame.locals import *
pygame.init()
import time
from random import randint

windowsize = 800
white = (255,255,255)
black = (0,0,0)
surface = pygame.display.set_mode((windowsize,windowsize))
run = True
t1 = 5
t2 = 15
t3 = 10
time1 = time.time()
wait_time = 10 #in seconds
boids = 20
boids_pos = []
for x in range(boids):
    boids_pos.append([randint(0, windowsize), randint(0, windowsize)])

def render():
    surface.fill(white)
    for x in range(boids):
        draw_boid(boids_pos[x][0],boids_pos[x][1])
        pygame.display.flip()

def update():
        for x in boids_pos:
            if x[0] > windowsize:
                x[0] = 0
            else:
                x[0]+=1

def draw_boid(x,y):
    pygame.draw.line(surface, black, (x,y), (x+t2,y+t1))
    pygame.draw.line(surface, black, (x,y+t3), (x+t2,y+t1))
    pygame.draw.line(surface, black, (x,y), (x,y+t3))

def flock_loop():
    global run
    global boids
    global time1
    while run:
        update()
        time2 = time.time()
        print("ooo")
        if (time2 - time1)%10 == 0:
            print("hi")
            render()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
flock_loop()