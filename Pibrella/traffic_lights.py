import pibrella
from time import sleep

SEQUENCE = [RED, RED_AMBER, GREEN, AMBER] = range(4)

TIMINGS = {
    RED: 3,
    RED_AMBER: 4,
    GREEN: 6,
    AMBER: 4
}

def action_red():
    pibrella.light.off()
    pibrella.light.red.on()

def action_red_amber():
    pibrella.light.off()
    pibrella.light.red.on()
    pibrella.light.amber.on()

def action_green():
    pibrella.light.off()
    pibrella.light.green.on()

def action_flashing_amber():
    pibrella.light.off()
    pibrella.light.amber.blink(0.5, 0.5)

def action_amber():
    pibrella.light.off()
    pibrella.light.amber.on()

ACTIONS = {
    RED: action_red,
    RED_AMBER: action_red_amber,
    GREEN: action_green,
    AMBER: action_amber
}

def traffic_lights():
    pibrella.light.off()
    for step in SEQUENCE:
        action = ACTIONS[step]
        dur = TIMINGS[step]
        action()
        sleep(dur)


traffic_lights()
