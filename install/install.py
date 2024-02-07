#first install git and tmux
#use tmux so you can scroll using ctrl-b then Page Up and Page Down keys - press q to exit the scroll mode
import os
import configparser
from helpers import (
    install_packages,
    flatpak_install,
    get_names,
    run_scripts,
    execute_command,
    current_path,
    refresh_dnf,
    update_system,
    copy_file
)

# # making sure script is running with sudo
if os.geteuid() != 0:
    print("This script requires sudo privileges.")
    exit()

### add my dot files
install_packages('stow')
execute_command('stow --adopt -d ~/.my_dotfiles -t ~/ .')
###
#configure dnf
dnfconfig = configparser.ConfigParser()
dnfconfig_path="/etc/dnf/dnf.conf"
dnfconfig.read(dnfconfig_path)

dnfconfig['main']['fastestmirror']="True"
dnfconfig['main']['max_parallel_downloads']="10"
dnfconfig['main']['defaultyes']="True"
dnfconfig['main']['keepcache']="True"

manager_dir=f"{current_path}/manager"

#write the new changes to dnf.conf
with open(dnfconfig_path, 'w') as configfile:
    dnfconfig.write(configfile)
# configuring dnf done

###
run_scripts('rpm-fusion') # it has to be done before anything cuz some installs depends on it
###
refresh_dnf()
###
update_system()
###
install_packages(*get_names(f"{manager_dir}/dnf"))
###
run_scripts(*get_names(f"{manager_dir}/scripts"))
###
run_scripts("flatpak")
flatpak_install(*get_names(f"{manager_dir}/flatpak"))
###
copy_file(f"{current_path}/files/50-mouse-acceleration.conf",'/etc/X11/xorg.conf.d/50-mouse-acceleration.conf')
### files that has to be executable
execute_command('chmod +x ~/.config/scripts/*')
execute_command('chmod +x ~/.config/bspwm/*')
execute_command('chmod +x ~/bin/*')

#scripts wait for some user input
run_scripts('oh-my-zsh')


