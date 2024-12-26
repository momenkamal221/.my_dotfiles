#!/bin/bash

# Array of keyboard layouts
layouts=("us" "eg")  # Add your desired layouts here

# Get the current layout
current_layout=$(setxkbmap -query | grep layout | awk '{print $2}')

# Find the index of the current layout
index=0
for i in "${!layouts[@]}"; do
  if [[ "${layouts[$i]}" == "$current_layout" ]]; then
    index=$i
    break
  fi
done

# Calculate the index of the next layout
next_index=$(( (index + 1) % ${#layouts[@]} ))

# Set the next layout
next_layout=${layouts[$next_index]}
setxkbmap "$next_layout"