
"""
Here you will be replacing the below implementation of a GCompound
with a new class which inherits from GCompound. Additionally, this
will allow you to implement more features into the class to add
options for changing color and movement.
"""

from pgl import GWindow, GRect, GLabel, GCompound
import random

def random_color():
    """ Returns a random hex color code. """
    col = "#"
    for _ in range(6):
        col += random.choice("0123456789abcdef")
    return col

# Define your new class here when you are ready



def create_object():
    """
    Creates the original DVD Logo. Code from here will be moved into
    the new class that you are creating.
    """

    width = 200
    height = 200

    obj = GCompound()

    cube = GRect(0,0,width,height)
    cube.set_filled(True)
    cube.set_color(random_color())
    obj.add(cube)

    dvdtext = GLabel("DVD")
    dvdtext.set_font("bold 60px 'serif'")
    obj.add(dvdtext,width/2-dvdtext.get_width()/2,height/2-10)

    vidtext = GLabel("video")
    vidtext.set_font("bold 50px 'serif'")
    vidtext.set_color("white")
    obj.add(vidtext, width/2-vidtext.get_width()/2, height/2+vidtext.get_ascent())

    return obj


gw = GWindow(800,600)
# Setting a black background so it looks like the tv
bg = GRect(0,0,gw.get_width(), gw.get_height())
bg.set_filled(True)
bg.set_color('black')
gw.add(bg)
# Create and add the logo
logo = create_object()
gw.add(logo, 300, 200)
