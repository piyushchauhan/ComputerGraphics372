from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 400                               # window size
x1, y1, x2, y2 = list(
    map(int, input("Enter x1, y1, x2, y2 separated by spaces:").split(" ")))


def drawLine(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    while abs(dx) > 1 or abs(dy) > 1:
        dx /= 2
        dy /= 2
    x, y = x1, y1
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    while abs(x2 - x) > 5:
        x = x + dx
        y = y + dy
        glVertex2f(x, y)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
    glColor3f(1.0, 1.0, 1.0)
    drawLine(x1, y1, x2, y2)
    glutSwapBuffers()


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(250, 200)
window = glutCreateWindow("Graphics Assignment 2")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
