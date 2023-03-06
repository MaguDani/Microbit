from microbit import *

import music
contador = 0
while True:
    if button_a.was_pressed():
        display.show(Image.ANGRY)
    elif button_b.was_pressed():
        music.play(music.DADADADUM)
