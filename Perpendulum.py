import pifacedigitalio
import time

listener = None
globalState = 'notReady'
pfd = pifacedigitalio.PiFaceDigital()


pfd.relays[0].value = 0
pfd.relays[1].value = 0
pfd.leds[0].turn_off()
pfd.leds[1].turn_off()
pfd.leds[7].turn_on()

pfd.leds[pfd.input_pins[1].value].turn_on()

print (pfd.input_pins[1].value)

def sensorLEDon(event):
    pfd.leds[3].turn_on()
    print (pfd.input_pins[1].value)
    activateMagnet('getReady')

def sensorLEDoff(event):
    pfd.leds[3].turn_off()
    print (pfd.input_pins[1].value)
    activateMagnet('go')

def fireMagnet():
    print ('Firing Magnet!')
    
    pfd.relays[1].value = 1
    time.sleep(.05)
    pfd.relays[1].value = 0
   
    
def activateMagnet(event):
    global globalState

    if event == 'getReady':
        globalState = 'ready'
        pfd.leds[4].turn_on()
    if (event == 'go' and globalState == 'ready'):
        fireMagnet()
        pfd.leds[4].turn_off()
        


listener = pifacedigitalio.InputEventListener()
listener.register(1, pifacedigitalio.IODIR_FALLING_EDGE, sensorLEDon)
listener.register(1, pifacedigitalio.IODIR_RISING_EDGE, sensorLEDoff)
listener.activate()
pfd.leds[7].turn_on()

