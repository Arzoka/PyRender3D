import numpy as np
import pygame


class Renderer:
    def __init__(self, window, camera):
        self.window = window
        self.surface = window.surface
        self.camera = camera

    def render(self, entity):
        if entity.object_type == 'solid':
            if len(entity.vertices) == 0:
                print('No vertices to render')
                return
            if len(entity.vertices[0]) < 3:
                print('Vertices must have at least 3 dimensions')
                return

            perspective_vertices = self.perspective_projection(entity.vertices, 200)
            plane_vertices = self.project_vertices(perspective_vertices)

            self.draw_faces(entity.faces, plane_vertices, entity.color)

    @staticmethod
    def perspective_projection(vertices, f):
        # TODO: Implement camera rotation, position, and fov
        returned_vertices = []

        for vertex in vertices:
            x, y, z = vertex[0], vertex[1], vertex[2]

            projection_matrix = np.array([
                [f / (f - z), 0, 0],
                [0, f / (f - z), 0],
                [0, 0, 1]
            ])

            point = np.array([x, y, z])
            projected_point = np.dot(projection_matrix, point)

            returned_vertices.append(projected_point)

        return returned_vertices

    @staticmethod
    def project_vertices(vertices):
        returned_vertices = []
        for vertex in vertices:
            x, y, z = vertex[0], vertex[1], vertex[2]

            _x = x * np.cos(0) - y * np.sin(0)
            _y = z + x * np.sin(0) + y * np.cos(0)

            returned_vertices.append([_x, _y])

        return returned_vertices

    def draw_faces(self, faces, vertices, color):
        for face in faces:
            face_vertices = [vertices[face[0]], vertices[face[1]], vertices[face[2]], vertices[face[3]]]

            self.draw_polygon(face_vertices, color)

    def draw_polygon(self, vertices, color):
        for i in range(len(vertices)):
            vertex = vertices[i]
            next_vertex = vertices[(i + 1) % len(vertices)]

            pygame.draw.line(
                self.surface,
                color,
                (vertex[0], vertex[1]),
                (next_vertex[0], next_vertex[1]),
                )

    def draw_pixel(self, x, y, color):
        print('drawing pixel at', x, y, 'with color', color)
        self.surface.set_at((int(x), int(y)), color)
