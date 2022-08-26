import time, pygame, DirStorage as storage, sys, time
from Main import black




X   = 1366
Y = 768
display = pygame.display
screen = display.set_mode((X, Y), pygame.FULLSCREEN)
background_colour = black
display.set_caption("Stack'em")
screen.fill(background_colour)

display.flip()