#!/bin/bash

# Check if Ulauncher is already running
if pgrep -x "ulauncher" > /dev/null
then
    ulauncher-toggle
else
    ulauncher --no-window-shadow
fi
