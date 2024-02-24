#!/bin/bash
#i made this script to escape the disktop '`'
# Get the ID of the current desktop 
# Get the current focused desktop ID
current_id=$(bspc query -D -d focused --names)
# Get the list of all occupied desktops
desktops=$(bspc query -D -d .occupied --names)
# Find the index of the current desktop in the list
current_index=$(echo "$desktops" | grep -n "$current_id" | cut -d ":" -f 1)
# Calculate the index of the next desktop
next_index=$((current_index % $(echo "$desktops" | wc -l) + 1))
# Get the name of the next desktop
next_id=$(echo "$desktops" | sed "${next_index}q;d")

if [ "$next_id" = '`' ]; then
bspc desktop -f '^1' 
else
bspc desktop -f next.occupied
fi

