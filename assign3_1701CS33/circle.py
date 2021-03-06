

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x0, y0, r = list(
    map(int, input("Enter x0, y0 , radius separated by spaces:").split(" ")))


def octCirclePts(x0, y0, x, y):
    # x, y is in octant 2 and are relative to x0,y0 that are centre coordinates
    glVertex2f(x0 + x, y0 + y)
    glVertex2f(x0 + x, y0 - y)
    glVertex2f(x0 - x, y0 + y)
    glVertex2f(x0 - x, y0 - y)

    glVertex2f(x0 + y, y0 + x)
    glVertex2f(x0 + y, y0 - x)
    glVertex2f(x0 - y, y0 + x)
    glVertex2f(x0 - y, y0 - x)


def drawCicle():
    glBegin(GL_POINTS)
    octCirclePts(x0, y0, 0, r)
    octCirclePts(x0, y0, r, 0)

    x, y, h = 0, r, 1-r
    while y > x:
        if h < 0:
            h += 2 * x + 3
        else:
            h += 2 * (x - y) + 5
            y -= 1
        x += 1
        octCirclePts(x0, y0, x, y)
    glEnd()
    glFlush()


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d

    glColor3f(1.0, 1.0, 1.0)                           # set color to blue
    drawCicle()
    # important for double buffering
    glutSwapBuffers()


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


window = 0                                             # glut window number
width, height = 500, 400                               # window size

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
# set window position
glutInitWindowPosition(250, 200)
# create window with title
window = glutCreateWindow("Graphics Assignment 1")
# set draw function callback
glutDisplayFunc(draw)
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything
