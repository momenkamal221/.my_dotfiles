#!/bin/bash

source .glob-vars.sh

# Function to turn on frame decorations
frame_decorations_on() {
    bspc config border_width 2
    picom-config corner-radius 10
    bspc config window_gap 5
    bspwm_frame_decoration=1
}

# Function to turn off frame decorations
frame_decorations_off() {
    bspc config border_width 2
    picom-config corner-radius 0
    bspc config window_gap 0
    bspwm_frame_decoration=0
}

# Check if argument is provided
if [ -z "$1" ]; then
    exit
fi

# Check the value of the argument and execute corresponding actions
if [ "$1" = "on" ]; then
    frame_decorations_on
elif [ "$1" = "off" ]; then
    frame_decorations_off
elif [ "$1" = "toggle" ]; then
    if [ "$bspwm_frame_decoration" -eq 0 ]; then
        frame_decorations_on
    else
        frame_decorations_off
    fi
elif [ "$1" = "stay" ]; then
    if [ "$bspwm_frame_decoration" -eq 0 ]; then
        frame_decorations_off
    else
        frame_decorations_on
    fi
fi

# Send a notification with the argument value
# Save the updated variable to the configuration file
glob-vars bspwm_frame_decoration=$bspwm_frame_decoration
