systemctl enable sddm
systemctl set-default graphical.target
xdg-user-dirs-update #to add the essensial folders of home directory
timedatectl set-timezone Africa/Cairo #for timezone
timedatectl set-ntp true
service ntpd start
systemctl enable ntpd
hostnamectl set-hostname momen-pc
