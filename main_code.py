import time # Import time for delays
from machine import Pin # Import Pin to control hardware

# Set up button on pin 15 as an input with a pull-down resistor
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
# Set up LED on pin 16 as an output
led = Pin(16, Pin.OUT)

# Start an infinite loop to keep the program running
while True:
    # Check if the button is pressed
    if button.value() == 1:
        time.sleep(0.1) # Short delay to handle button bounce
  
        # Wait and check the button state over a 2-second period
        for i in range(3600):
            time.sleep(1) # Wait 1 second
            # If button is pressed again during this time, exit the loop
            if button.value() == 1:
                break
        # If the loop finishes without breaking (button wasn't pressed again)
        else:
            # Start an infinite loop to blink the LED
            while True:
                led.value(1)    # Turn the LED on
                time.sleep(0.1) # Wait for 0.1 seconds
                # Stop blinking if the button is pressed
                if button.value() == 1: break
                
                led.value(0)    # Turn the LED off
                time.sleep(0.1) # Wait for 0.1 seconds
                # Stop blinking if the button is pressed
                if button.value() == 1: break