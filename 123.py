from microbit import *

while True:
    display.show("2")
    if button_a.is_pressed():
        display.show("1")
        sleep(1)
    elif button_b.is_pressed():
        display.show("3")
        sleep(1)
        
