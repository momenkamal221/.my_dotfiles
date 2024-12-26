#!/bin/bash
git clone https://github.com/catppuccin/sddm.git ~/sddm-themes
sudo cp -r  ~/sddm-themes/src/* /usr/share/sddm/themes/
rm -rf ~/sddm-themes