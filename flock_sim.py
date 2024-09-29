import pygame
from pygame.locals import *

import AppKit

class AppDelegate(AppKit.NSApplication):
    def applicationSupportsSecureRestorableState(self):
        return True
    
#class AppKit.NSApplication:
    #def applicationSupportsSecureRestorableState(self):
        #return True


pygame.init()

windowsize =800
white = (225,225,225)

surface = pygame.display.set_mode((windowsize,windowsize))
surface.fill(white)

pygame.display.flip