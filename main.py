import pygame
from pygame import *
import tools
pygame.init()
width = 720
height = width/16*9

dark_mode = True
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("UNO Remake")

dark_mode_image = pygame.transform.scale(pygame.image.load("Assets/dark_mode.png").convert_alpha(), (100, 100))
light_mode_image = pygame.transform.scale(pygame.image.load("Assets/light_mode.png").convert_alpha(), (100, 100))

clock = pygame.time.Clock()
while True:
    if dark_mode:
        screen.fill((18,18,18))
    else:
        screen.fill((237, 237, 237))
    play = tools.Button(width / 4, height / 4 - height / 16, width / 2, height / 4, "Jouer", "#FFFFFF", "#0077B6", "#26486D", 50)
    rules = tools.Button(width / 4, height / 2 + height / 16, width / 2, height / 4, "Règles", "#FFFFFF", "#0077B6", "#26486D", 50, action=tools.open_rules)
    dark_mode_button = tools.Button_dark_mode(width - 100, 10, dark_mode, dark_mode_image, light_mode_image)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == VIDEORESIZE:
            width = event.w
            height = event.h
        dark_mode_button.update(event)
    dark_mode_button.draw(screen)
    screen.blit(pygame.font.SysFont(None, 30).render(f"Mouse pos: {pygame.mouse.get_pos()}", True, (255, 255, 255)), (10, 10))
    play.draw(screen)
    rules.draw(screen)
    dark_mode = dark_mode_button.get_state()
    
    pygame.display.update()
    clock.tick(60)
