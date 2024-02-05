# Dependencies
import time
import pygame

from entities.camera import Camera
from helpers.keybind_listener import listen_for_keybinds
# Helpers
from helpers.read_json import read_json

# Entities
from entities.window import Window
from entities.renderer import Renderer
from entities.object import Object

if __name__ == '__main__':
    Config = read_json('config/config.json')

    # Entities
    window = Window(Config)
    camera = Camera()

    renderer = Renderer(window, camera)

    Cube = Object(
        object_type='solid',
        vertices=[
            [0, 0, 0],
            [100, 0, 0],
            [100, 100, 0],
            [0, 100, 0],
            [0, 0, 100],
            [100, 0, 100],
            [100, 100, 100],
            [0, 100, 100]
        ],
        faces=[
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [0, 3, 7, 4],
            [1, 2, 6, 5]
        ],

        color=pygame.color.Color('green')
    )

    renderer.render(Cube)

    # Main loop
    while window.running:
        listen_for_keybinds()
        window.update()
        time.sleep(1 / window.fps)
