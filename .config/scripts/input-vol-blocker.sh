#!/bin/bash
while sleep 0.1; 
do 
pactl set-source-volume $(pactl list short sources | grep input | cut -d'	' -f1) 30%
done
