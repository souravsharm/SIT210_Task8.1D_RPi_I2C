import busio
import time
import board
import adafruit_veml7700

# sudo pip3 install adafruit-circuitpython-veml7700
# VEML7700:
#       Pi 3V3(PIN-1) to sensor VIN
#       Pi GND(PIN-6) to sensor GND
#       Pi SCL(PIN-5) to sensor SCL
#       Pi SDA(PIN-3) to sensor SDA

i2c = busio.I2C(board.SCL, board.SDA)
veml7700 = adafruit_veml7700.VEML7700(i2c)


 
while True:
    amb_light = veml7700.light
    
    print("Ambient light:", amb_light)
    
    # highlights the light mode
    
    if amb_light > 18000:
        print ("blinding bright")
    elif amb_light > 16000:
        print ("bright")
    elif amb_light > 10000:
        print ("medium")
    elif amb_light > 5000:
        print ("dark")
    else :
        print ("glaring dark")
    time.sleep(0.1)