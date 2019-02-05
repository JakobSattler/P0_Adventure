import sys
import pygame
from pygame.locals import *
from player import Player

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = None
background = None
player = Player()

running = True

objectSpeed = 5

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
            checkInput(event)

        player.update()
        background.blit(player.rect, player.rect)

        screen.blit(background, (0, 0))
        pygame.display.flip()

def checkInput(event):
    # close game
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
        global running
        running = False

    # player movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == ord("a"):
            player.moveLeft()
        if event.key == pygame.K_RIGHT or event.key == ord("d"):
            player.moveRight()
        if event.key == pygame.K_UP or event.key == ord("w"):
            player.moveUp()
        if event.key == pygame.K_DOWN or event.key == ord("s"):
            player.moveDown()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == ord("a"):
            player.stopLeft()
        if event.key == pygame.K_RIGHT or event.key == ord("d"):
            player.stopRight()
        if event.key == pygame.K_UP or event.key == ord("w"):
            player.stopUp()
        if event.key == pygame.K_DOWN or event.key == ord("s"):
            player.stopDown()
