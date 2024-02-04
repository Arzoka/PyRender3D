import pygame


class Window:
    def __init__(self, config):
        self.running = True
        self.width = config["window"]["width"]
        self.height = config["window"]["height"]
        self.title = config["title"]
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.surface = pygame.Surface((self.width, self.height))
        self.fps = config["window"]["fps"]

    def update(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.fps)
