#!/bin/bash
# Start your process with the highest priority
nice -n -20 your_command_here &
# Get the process ID of the started process
pid=$!
# Give the process and its children the highest priority
renice -n -20 -p $pid

vol=5
movemousefast() {
	if [[ $x -ne 0 && $y -ne 0 ]]; then
		for ((i = 0; i < 100; i++)); do
			xdotool mousemove 0 0
			xdotool mousemove $1 $2 &
		done
	fi
}
cursor_position=$(xdotool getmouselocation --shell)
eval "$cursor_position"
x=$X
y=$Y
movemousefast $x $y 3 &

if [ $1 == "up" ]; then
	current_volume=$(amixer sget Master | awk -F"[][]" '/Left:/ { print $2 }')
	current_volume=${current_volume%\%}
	next_volume=$((current_volume + 5))
	# Check if volume exceeds 100%
	if [[ $next_volume -gt 100 ]]; then
		vol_amount="+$((100 - current_volume))%"
	else
		vol_amount="+$vol%"

	fi
elif [ $1 == "down" ]; then
	vol_amount="-$vol%"
fi
pactl set-sink-volume @DEFAULT_SINK@ "$vol_amount"
play $scripts/audio-volume-change.oga &
