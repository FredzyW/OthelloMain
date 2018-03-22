
import pyglet
from pyglet.gl import *
from pyglet.window import key
from math import *

window = pyglet.window.Window()



text_label = pyglet.text.Label('OTHELLO',
                         font_name='Comic Sans',
                         font_size=50,
                         x=window.width // 2, y=window.height // 2 + 200,
                         anchor_x='center', anchor_y='center')


spelar_position = [window.width//2, window.height//2]

@window.event
def on_draw():

    window.clear()

    text_label.draw()

    posx, posy = 0, 0
    sides = 32
    radius = 1
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()


pyglet.app.run()