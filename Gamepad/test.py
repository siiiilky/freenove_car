# Gamepad testing
# Steven Coutts - 16/08/2020
# stevec@couttsnet.com

import inputs

pads = inputs.devices.gamepads
if len(pads) == 0:
    raise Exception("Couldn't find any Gamepads!")
while True:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)