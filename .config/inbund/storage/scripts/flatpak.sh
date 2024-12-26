#!/bin/bash
# https://itsfoss.com/flatpak-app-apply-theme/
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
sudo flatpak override --filesystem=$HOME/.themes
sudo flatpak override --filesystem=$HOME/.icons

sudo flatpak override --filesystem=/usr/share/.themes
sudo flatpak override --filesystem=/usr/share/.icons

#gtk
sudo flatpak override --env=GTK_THEME=Arc-Dark
sudo flatpak override --env=ICON_THEME=Papirus-Dark

#qt
sudo flatpak override --filesystem=xdg-config/Kvantum:ro
sudo flatpak override --env=QT_STYLE_OVERRIDE=kvantum