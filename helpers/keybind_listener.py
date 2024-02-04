import pygame


def listen_for_keybinds():
    mouse = pygame.mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
