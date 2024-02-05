#!/bin/bash
out=$(stow --adopt -d ~/.my_dotfiles -t ~/ . 2>&1)
echo $out
if [[ -n $out ]]; then
	paplay /usr/share/sounds/freedesktop/stereo/dialog-warning.oga &
    notify-send "Stow: check ~/.my_dotfiles/.stow-log"
	echo -ne "\n\n\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n$(date)\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n$out" >> ~/.my_dotfiles/.stow-log
fi
