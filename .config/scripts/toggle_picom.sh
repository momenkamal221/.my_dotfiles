#!/bin/bash

# Check if picom is running
if pgrep -x "picom" > /dev/null
then
		pkill picom
else
    picom --config $picom &
fi
