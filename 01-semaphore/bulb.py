from PIL import Image, ImageTk
from tkinter import Label
import numpy as np
import colorsys

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)
offhue = 0.33

def shift_hue(arr, hout, sout, vout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    if sout != None:
        s.fill(sout)
    if hout != None:
        h.fill(hout)
    if vout != None:
        v *= vout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def colorize(image, hue, sat, val):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360., sat, val).astype('uint8'), 'RGBA')

    return new_img

colors = {
    'red': 0,
    'yellow': 45,
    'green': 120,
    'blue': 240,
}

class Bulb:
    def __init__(self, parent, position, color='blue', state='off'):
        self.parent = parent
        self.path = './images/bulb.png'
        self.image = Image.open(self.path)
        self.image = self.image.resize((80,80), Image.ANTIALIAS)
        self.color = 0
        self.on = False
        self.label = Label(self.parent)
        self.label.place(x=position[0], y=position[1])
        
        self.set_state(state)
        self.set_color(color)

        self.prevon = True
        self.prevcolor = -1 

        self.update()

    def set_color(self, color):
        global colors

        if color not in colors:
            raise Exception('Color must be yellow/red/green/blue.')
        self.color = colors[color]

    def set_state(self, state):
        if state != 'on' and state != 'off':
            raise Exception('State must be on/off.')
        self.on = state == 'on'

    def update(self):
        global colorize, offhue
        if self.prevcolor == self.color and self.prevon == self.on:
            return

        self.image = colorize(self.image, self.color, 0.+self.on,None if self.prevon == self.on else 1./offhue if self.on else offhue)
        image = ImageTk.PhotoImage(self.image)
        self.label['image'] = image
        image.image = image

        self.prevon = self.on
        self.prevcolor = self.color