#!/bin/bash
sudo dnf swap ffmpeg-free ffmpeg --allowerasing -y

sudo dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin -y
sudo dnf groupupdate sound-and-video -y
sudo dnf install lame\* --exclude=lame-devel -y
sudo dnf install vlc mpv -y
