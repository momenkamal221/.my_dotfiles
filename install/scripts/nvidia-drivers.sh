#!/bin/bash
sudo dnf update -y # and reboot if you are not on the latest kernel
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda libva libva-nvidia-driver -y #optional for cuda/nvdec/nvenc support
