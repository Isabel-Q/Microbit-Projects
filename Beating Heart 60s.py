from microbit import *

heart = Image.HEART

while running_time() < 60000:
    for i in range(10):
        heart1 = heart * 0.1 * i
        display.show(heart1)
        sleep(100)
        
display.clear()