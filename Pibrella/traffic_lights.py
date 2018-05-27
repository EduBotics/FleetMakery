import pibrella
from time import sleep

SEQUENCE = [RED, RED_AMBER, GREEN, AMBER] = range(4)

TIMING = {
    RED: 3,
    RED_AMBER: 4,
    GREEN: 6,
    AMBER: 4
}

ACTIONS = {
    RED: pibrella.light.red.on,
    RED_AMBER: lambda: pibrella.light.off() && pibrella.light.red.on() && pibrella.light.amber.on(),
    GREEN: pibrella.light.green.on,
    AMBER: pibrella.light.amber.blink(0.5,0.5)
}

def traffic_lights():
    pibrella.light.off()
    for step in SEQUENCE:
        action = ACTIONS[step]
        dur = TIMINGS[step]
        action()
        sleep(dur)


traffic_lights()
