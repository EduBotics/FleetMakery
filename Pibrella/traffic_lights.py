import pibrella
from time import sleep

def traffic_lights():
    pibrella.light.off()
    pibrella.light.red.on()
    sleep(3)
    pibrella.light.amber.on()
    sleep(4)
    pibrella.light.off()
    pibrella.light.green.on()
    sleep(6)
    pibrella.light.off()
    pibrella.light.amber.blink(0.5,0.5)
    sleep(4)
    pibrella.light.off()

traffic_lights()
