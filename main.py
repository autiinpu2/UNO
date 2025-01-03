import pygame
from pygame import *
import tools
pygame.init()
width = 720
height = width/16*9

dark_mode = True
bg_color = (18,18,18)
dark_color = (18,18,18)
light_color = (237, 237, 237)

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("UNO Remake")

dark_mode_image = pygame.transform.scale(pygame.image.load("Assets/dark_mode.png").convert_alpha(), (50, 50))
light_mode_image = pygame.transform.scale(pygame.image.load("Assets/light_mode.png").convert_alpha(), (50, 50))


clock = pygame.time.Clock()
while True:
    bg = tools.Background(dark_color, light_color, dark_mode).draw(screen)
    play = tools.Button(width / 4, height / 4 - height / 16, width / 2, height / 4, "Jouer", "#FFFFFF", "#0077B6", "#26486D", 50)
    rules = tools.Button(width / 4, height / 2 + height / 16, width / 2, height / 4, "Règles", "#FFFFFF", "#0077B6", "#26486D", 50, action=tools.open_rules)
    dark_mode_button = tools.Button_dark_mode(width - width/9.6, height/16.2, width, height, dark_mode, dark_mode_image, light_mode_image)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == VIDEORESIZE:
            width = event.w
            height = event.h
            dark_mode_image = pygame.transform.scale(pygame.image.load("Assets/dark_mode.png").convert_alpha(), (width/14.4, height/8.1))
            light_mode_image = pygame.transform.scale(pygame.image.load("Assets/light_mode.png").convert_alpha(), (width/14.4, height/8.1))
        dark_mode_button.update(event)
    dark_mode_button.draw(screen)
    screen.blit(pygame.font.SysFont(None, 30).render(f"Mouse pos: {pygame.mouse.get_pos()}", True, (255, 255, 255)), (10, 10))
    play.draw(screen)
    rules.draw(screen)
    dark_mode = dark_mode_button.get_state()
    
    pygame.display.update()
    clock.tick(60)
