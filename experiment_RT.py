from triggerbox import *
from psychopy import core

# connect to the trigger box via serial port
trigger = TriggerBox()

# send a 5V signal over analog channel 3 for 100 ms
go = trigger.make_analog_signal(channel = 3, voltage = 5, duration = 100)
# send the signal
trigger.ser.write(go) 


# close the serial connections
trigger.ser.close()
output.close()
