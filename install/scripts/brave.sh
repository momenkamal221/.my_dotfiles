#!/bin/bash
sudo dnf install dnf-plugins-core -y

sudo dnf config-manager --add-repo https://brave-browser-rpm-beta.s3.brave.com/brave-browser-beta.repo  -y

sudo rpm --import https://brave-browser-rpm-beta.s3.brave.com/brave-core-nightly.asc

sudo dnf install brave-browser-beta  -y
