from microbit import *

centre = Image("00700:""00700:""00700:""00700:""00700:")
right1 = Image("00070:""00070:""00070:""00070:""00070:")
left1 = Image("07000:""07000:""07000:""07000:""07000:")
right2 = Image("00007:""00007:""00007:""00007:""00007:")
left2 = Image("70000:""70000:""70000:""70000:""70000:")

screen = 1

while screen == 1:
    
    reading = accelerometer.get_x()
    
    if reading > 30 and reading < 60:
        display.show(right1)
    elif reading <-30 and reading >-60:
        display.show(left1)
    elif reading > 60:
        display.show(right2)
    elif reading < -60:
        display.show(left2)
        
    elif button_a.is_pressed() and button_b.is_pressed():
        screen = 0
        
    else:
        display.show(centre)

display.clear()
