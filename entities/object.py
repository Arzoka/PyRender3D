import pygame


class Object:
    def __init__(self, object_type, vertices, faces, color):
        self.object_type = object_type
        self.vertices = vertices
        self.faces = faces
        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.scale = self.getsize(vertices)

        if color:
            self.color = color
        else:
            self.color = pygame.color.Color('white')

    @staticmethod
    def getsize(vertices):
        x = []
        y = []
        z = []
        for vertex in vertices:
            x.append(vertex[0])
            y.append(vertex[1])
            z.append(vertex[2])
        return [max(x) - min(x), max(y) - min(y), max(z) - min(z)]
