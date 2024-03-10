#!/bin/bash
#1-for each chunk, scroll <scroll_number> times
#2- scroll for <times> times, the sleep time is from <sleep_time_init> to 0 for depending on the number of chunks"
scroll_by_freq=$1 #second mode off/on
chunk=20         #chunk size
# 1- changing the following doesn't make any difference if you are using the second mode
scroll_number=1 # how many scrolls for each chunk passed ,will be used only on the first mode
sleep_time=0.1  #defualt value for the first mode
# 2- changing the following doesn't make any difference if you are using the first mode
times=1              #is defualt value for the total scroll number for the second mode
sleep_time_init=1.25 #sleep time on
sleep_time_min=0.01
sleep_time_step=0.05
minimum_magnitude_y=50
source ~/.glob-vars.sh
#functions
stop-scrolling-mode() {
	glob-vars scroll_mode=0
}
start-scrolling-mode() {
	glob-vars scroll_mode=1
}
fire-scroll-up() {
	for ((i = 0; i < $1; i++)); do
		xdotool click 4 &
	done
}
fire-scroll-down() {
	for ((i = 0; i < $1; i++)); do
		xdotool click 5 &
	done
}
abs() {
	echo $(echo "scale=3; sqrt($1^2)" | bc | xargs printf "%.3f")
}
clamp() {
	local value=$1
	local min=$2
	local max=$3
	if (($(echo "scale=3; $value < $min" | bc -l))); then
		echo $min
	elif (($(echo "scale=3; $value > $max" | bc -l))); then
		echo $max
	else
		echo $value
	fi
}

cursor_position=$(xdotool getmouselocation --shell)
eval "$cursor_position"
y=$Y

if [[ $scroll_mode -eq 1 ]]; then
	stop-scrolling-mode
	exit
else
	start-scrolling-mode
fi

while true; do
	source ~/.glob-vars.sh
	if [[ $scroll_mode -eq 0 ]]; then
		exit
	fi

	cursor_position=$(xdotool getmouselocation --shell)
	eval "$cursor_position"
	y_current=$Y
	magnitude_y=$((y_current - y))
	magnitude_y_abs=$(echo "scale=3; sqrt($magnitude_y^2)" | bc)
	magnitude_y_abs=${magnitude_y_abs%.*}
	if [ $magnitude_y_abs -lt $minimum_magnitude_y ]; then
		continue
	fi
	if [[ $scroll_by_freq -eq 1 ]]; then
		chunks_passed=$(abs $(echo "scale=3; $magnitude_y / $chunk" | bc | xargs printf "%.3f"))
		sleep_time=$(echo "scale=3; $sleep_time_init - ($chunks_passed * $sleep_time_step)" | bc | xargs printf "%.3f")
		sleep_time=$(clamp $sleep_time $sleep_time_min $sleep_time_init)
	else
		times=$(echo "$magnitude_y * $scroll_number / $chunk" | bc)
		times=$(echo "sqrt($times^2)" | bc)
		times=${times%.*}
	fi

	if [[ $magnitude_y -gt 0 ]]; then
		fire-scroll-down $times

	elif [[ $magnitude_y -lt 0 ]]; then
		fire-scroll-up $times

	fi
	sleep $sleep_time
	# xdotool mousemove_relative -- $(($x_current-$x)) $(($y_current-$y))
done

trap "stop-scrolling-mode; exit" 15
trap "stop-scrolling-mode; exit" 3
trap "stop-scrolling-mode; exit" 2
trap "stop-scrolling-mode; exit" 0
