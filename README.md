# Making a flock simulator

## What I need to figure out
* Steps to start
* How to create the flocks
* How to make them move
* How to get them to flock
* Vectors

## Stuff to know
### Vectors
Vectors have a magnitude and direction. A vector is a line segment, the magnitude is length between its tail and its head and direction is from it's tail to its head. 
### Rotating vectors/a triangle
Formula Overview

Given three points:
- `P1(x1, y1)`
- `P2(x2, y2)`
- `P3(x3, y3)`

We calculate the angle of rotation between the vectors:
- `v1 = (x2 - x1, y2 - y1)`  
- `v2 = (x3 - x1, y3 - y1)`

Steps:
1. **Calculate the dot product:**
   \[
   \text{dot\_product} = (x2 - x1)(x3 - x1) + (y2 - y1)(y3 - y1)
   \]

2. **Calculate the magnitudes:**
   \[
   \|v1\| = \sqrt{(x2 - x1)^2 + (y2 - y1)^2}
   \]
   \[
   \|v2\| = \sqrt{(x3 - x1)^2 + (y3 - y1)^2}
   \]

3. **Calculate the angle in radians:**
   \[
   \cos(\theta) = \frac{\text{dot\_product}}{\|v1\| \|v2\|}
   \]
   \[
   \theta = \cos^{-1}(\cos(\theta))
   \]

4. **Convert to degrees:**
   \[
   \text{angle (degrees)} = \theta \times \frac{180}{\pi}
   \]

## Work
### Latest Update 10/11/2024
Somehow pygame is now working without AppKit or I may have disabled AppKit somehow. I wouldn't know; I am relatively new to coding. So I will be progressing the project now.
#### Boids point different directions and go in that direction
This will require some geometry and vector knowledge.
#### *Done* Game loop
Every ten seconds render updated progress of the movement of boids. Update and render need to be seperate. 

### Update 29/09/2024
Pygame is not working on macs without AppKit. So I will be taking a break from the project until I learn more about classes and find another way to render the simulator.
#### First order of business
Well, I have to make some polygons appear on the screen. So I need to create a screen and I need to create some polygons. The polygons should be randomly placed but equal in size and dimensions. I have seen arrow style flocks used so will copy that shape. They are aethetically pleasing. For now, I will create a white screen and black flocks.

## Glossary

### Magnitude
### Unit Vector
### 