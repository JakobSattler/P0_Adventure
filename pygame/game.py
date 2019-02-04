import pygame
from pygame.locals import *
from player import Player

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = None
background = None
player = Player()

running = True

def start():
    init()
    startGame()

def init():
    pygame.init()

    # set initial player position
    player.rect = pygame.Rect(20, 20, 20, 20)

    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("P0_Adventure")

    # init background
    global background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((133,133,133))

    # some text
    font = pygame.font.Font(None, 50)
    text = font.render("Test", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    # blit to screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

def startGame():
    running = True
    runLoop()

def runLoop():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        pygame.draw.rect(background, (0, 255, 0), player.rect)

        screen.blit(background, (0, 0))
        pygame.display.flip()
