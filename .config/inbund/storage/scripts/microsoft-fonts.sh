#!/bin/bash
sudo dnf install curl cabextract xorg-x11-font-utils fontconfig  -y
sudo rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm
sudo dnf install dejavu-fonts-all google-noto-sans-fonts google-noto-serif-fonts google-noto-cjk-fonts google-noto-emoji-fonts dejavu-sans-fonts dejavu-serif-fonts gdouros-symbola-fonts gnu-free-serif-fonts unifont cjkuni-ukai-fonts cjkuni-uming-fonts  liberation-fonts google-noto-sans-javanese-fonts -y

rm -rf ~/.cache/fontconfig #deletes the font cache
fc-cache -r -v #rebuilds the font cache




