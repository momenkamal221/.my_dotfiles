#!/bin/bash

while true; do
    sleep 0.1
    caps_state=$(xset q | grep "Caps Lock" | awk '{print $4}')
    # Check if the file caps.lock exists
    if [ -f "$scripts/caps.lock" ]; then
        if [ "$caps_state" == "on" ]; then
            xdotool key Caps_Lock
        fi
			else
			if [ "$caps_state" == "off" ]; then
            xdotool key Caps_Lock
        fi
    fi
done

