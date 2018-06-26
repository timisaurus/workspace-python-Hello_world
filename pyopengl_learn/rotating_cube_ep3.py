import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

vertices = (
    (1, 1, 1),  # 0
    (-1, 1, 1),  # 1
    (1, -1, 1),  # 2
    (1, 1, -1),  # 3
    (-1, -1, 1),  # 4
    (-1, 1, -1),  # 5
    (1, -1, -1),  # 6
    (-1, -1, -1),  # 7
)

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (4, 1),
    (4, 2),
    (4, 7),
    (5, 1),
    (5, 3),
    (5, 7),
    (6, 2),
    (6, 3),
    (6, 7)
)

surfaces = (
    (1, 0, 2, 4),
    (1, 0, 3, 5),
    (2, 0, 3, 6),
    (4, 1, 5, 7),
    (4, 2, 6, 7),
    (5, 3, 6, 7),
)

colors = (
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 1, 1),
    (1, 1, 0),
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 1, 1),
    (1, 1, 0),
    (1, 1, 1)

)


def cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (640, 480)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -40.0)  # makes cube move

    glRotatef(0, 0, 0, 0)

    object_passed = False

    glEnable(GL_DEPTH_TEST)  # makes cube solid

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)

        #                if event.button == 4:
        #                    glTranslatef(0,0,1)
        #                if event.button == 5:
        #                    glTranslatef(0,0,-1)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_z = x[3][0]
        camera_z = x[3][1]
        camera_z = x[3][2]

        if camera_z < -1:
            object_passed = True

        # glRotatef(1, 3, 1, 1)  # Makes Cube rotate
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glTranslatef(0, 0, .50)

        cube()
        pygame.display.flip()
        pygame.time.wait(10)


for x in range(10):
    main()
main()
pygame.quit()
quit()
