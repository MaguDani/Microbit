# Imports go at the top
from microbit import *

# Variable contador
nombre = "Daniel"

while True:
    display.show(Image.GHOST)
    sleep(2000)
    display.scroll(nombre)