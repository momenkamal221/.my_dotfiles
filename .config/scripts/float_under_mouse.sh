#!/bin/bash

# Get the active window ID
active_win_id=$(xdotool getactivewindow)

# Get the mouse coordinates
eval $(xdotool getmouselocation --shell)

# Move the active window to the mouse coordinates
xdotool windowmove $active_win_id $X $Y
