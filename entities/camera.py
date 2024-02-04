class Camera:
    def __init__(self):
        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.fov = 90

    def move(self, position):
        self.position = position

    def rotate(self, rotation):
        self.rotation = rotation

    def set_fov(self, fov):
        self.fov = fov
