# -*- coding: latin-1 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import os
import time
import json


from rgbmatrix import Adafruit_RGBmatrix

width = 64  # Matrix size (pixels) -- change for different matrix
height = 32  # types (incl. tiling).  Other code may need tweaks.
matrix         = Adafruit_RGBmatrix(32, 2) # rows, chain length
fps = 4

font = ImageFont.load(os.path.dirname(os.path.realpath(__file__))
                      + '/helvR08.pil')

blancColor = (255, 255, 255)  # Blanc

# Drawing takes place in offscreen buffer to prevent flicker
image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(image)
currentTime = 0.0
prevTime = 0.0

# Initialization done; loop forever ------------------------------------------

text1Pos = -10000
text2Pos = -10000

def changeTextPos(textPos, text):
    if textPos == -10000:
        textPos = 64
    if textPos < -(len(text) * 4) - 4:
        textPos = 64
    return textPos

def display(text1, text2, text3, text4):
    global text1Pos
    global text2Pos

    if len(text1) > len(text2):
        text1Eval = text1
    else:
        text1Eval = text2

    if len(text3) > len(text4):
        text2Eval = text3
    else:
        text2Eval = text4

    text1Pos = changeTextPos(text1Pos, text1Eval)
    text2Pos = changeTextPos(text2Pos, text2Eval)

    draw.text((-4 + text1Pos, -2), ' ' + text1 + ' ', font=font, fill=(blancColor))
    draw.text((-4 + text1Pos, 6), ' ' + text2 + ' ', font=font, fill=(blancColor))
    draw.text((-4 + text2Pos, 14), ' ' + text3 + ' ', font=font, fill=(blancColor))
    draw.text((-4 + text2Pos, 23), ' ' + text4 + ' ', font=font, fill=(blancColor))

    text1Pos -= 1
    text2Pos -= 1
while True:

    # Clear background
    draw.rectangle((0, 0, width, height), fill=(0, 0, 0))

    display("Projet Hub", "14h - U", "Desk", "14h")

    # Offscreen buffer is copied to screen
    matrix.SetImage(image.im.id, 0, 0)

    # debug
    #image.save("tmp.png")  # image.show()

    # wait
    currentTime = time.time()
    timeDelta = (1.0 / fps) - (currentTime - prevTime)
    if (timeDelta > 0.0):
        time.sleep(timeDelta)
    prevTime = currentTime