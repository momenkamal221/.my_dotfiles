#!/bin/bash
# Get the sink index
sink_index=$(pactl list short sinks | awk '{print $1}')

# Get the mute status
mute_status=$(pactl list sinks | grep -A 10 "Sink #$sink_index" | awk '/Mute/{print $2}')

# Toggle mute
if [ "$mute_status" == "yes" ]; then
	pactl set-sink-mute "$sink_index" 0
	echo "Unmuted"
else
	pactl set-sink-mute "$sink_index" 1
	echo "Muted"
fi
