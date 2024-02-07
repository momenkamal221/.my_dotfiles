#!/usr/bin/env python3
# i made this script because of the wm's that its shortcuts doesn't work when the keyboard is arabic
# /home/momen/.config/bspwm/scripts/layout-switcher.py us ara
from pynput import keyboard
import os
import sys
os.system('setxkbmap -layout ' + sys.argv[1])
mods={
    'alt':False,
    'ctrl':False,
    'cmd':False,
}
keyPressed=''
def is1ModPressed():
    result=False
    for key, value in mods.items():
        result = result or value
    return result
def isModPressed(mod):
    return mods[mod]
def modPress(mod):
    mods[mod]=True
def modRelease(mod):
    mods[mod]=False
import os

def get_current_layout_name():
    # Command to get the current keyboard layout
    layout_command = "setxkbmap -query |  awk '/layout/ {print $2}'"
    # Run the command using os.popen()
    layout = os.popen(layout_command).read()
    return layout.replace('\n','')

def get_current_layout_index():
    layout=get_current_layout_name()
    return sys.argv[1:].index(layout)


kbdcfg = {
    'cmd': 'setxkbmap',
    'layout': sys.argv[1:],
    'current': get_current_layout_index()
}


# Function to switch keyboard layout
def switch_layout():
    kbdcfg['current'] = (kbdcfg['current'] + 1) % len(kbdcfg['layout'])
    layout = kbdcfg['layout'][kbdcfg['current']]
    # os.system(kbdcfg['cmd']+ ' ' + layout)


# Function to execute when Mod4 is pressed
def on_mod_down():
    # Add your code to execute when Mod4 is pressed
    os.system('setxkbmap us')

# Function to execute when Mod4 is released
def on_mod_up():
    # Add your code to execute when Mod4 is released
    layout = kbdcfg['layout'][kbdcfg['current']]
    os.system(kbdcfg['cmd']+ ' ' + layout)



# Define your functions to be called when keys are pressed or released
def on_press(key):
    global keyPressed
    if key == keyboard.Key.cmd:
        modPress('cmd')
    elif key == keyboard.Key.ctrl:
        modPress('ctrl')
    elif key == keyboard.Key.alt:
        modPress('alt')
    else:
        try:
            keyPressed=key.char
        except:
            pass

    if is1ModPressed():
        on_mod_down()
    #hotkeys
    if isModPressed('cmd') and keyPressed==';':
        switch_layout()


def on_release(key):
    global keyPressed
    if key == keyboard.Key.cmd:
        modRelease('cmd')
    elif key == keyboard.Key.ctrl:
        modRelease('ctrl')
    elif key == keyboard.Key.alt:
        modRelease('alt')
    else:
        try:
            keyPressed=''
        except:
            pass

    if not is1ModPressed():
        on_mod_up()


# Create listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
