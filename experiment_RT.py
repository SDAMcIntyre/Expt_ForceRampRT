from triggerbox import *
from psychopy import core
import win32api

# https://stackoverflow.com/questions/41688871/python-check-if-mouse-clicked


#### SETUP ####

# number of times to trigger the stimulus and record the reaction time
nTrials = 3

# connect to the trigger box via serial port
trigger = TriggerBox()

# trigger signal: 5V signal over analog channel 3 for 100 ms
go = trigger.make_analog_signal(channel = 3, voltage = 5, duration = 100)

stopwatch = core.Clock()

#### EXPERIMENT ####

for trial in range(nTrials):
    print("Get ready...")
    core.wait(1.5)
    mousePressed = False # reset mouse detection
    stopwatch.reset() # start stopwatch
    #trigger.ser.write(go) # send the signal
    while not mousePressed:
        mouseState = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128
        if mouseState < 0: mousePressed = True

    reactionTime = stopwatch.getTime()
    print("Trial {}, reaction time = {} sec" .format(trial+1,reactionTime))


#### END ####

trigger.ser.close()
core.quit()
