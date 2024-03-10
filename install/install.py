#first install git and tmux
#use tmux so you can scroll using ctrl-b then Page Up and Page Down keys - press q to exit the scroll mode
import os
import configparser
import dnf
from helpers import (
    install_packages,
    flatpak_install,
    get_names,
    run_scripts,
    execute_command,
    current_path,
    refresh_dnf,
    update_system,
    copy_file,
    remove_packages,
    manager_dir
)

# # making sure script is running with sudo
if os.geteuid() != 0:
    print("This script requires sudo privileges.")
    exit()


execute_command('mkdir ~/.config')


###
#configure dnf
dnfconfig = configparser.ConfigParser()
dnfconfig.optionxform = str
dnfconfig_path="/etc/dnf/dnf.conf"
dnfconfig.read(dnfconfig_path)

dnfconfig['main']['fastestmirror']="True"
dnfconfig['main']['max_parallel_downloads']="10"
dnfconfig['main']['defaultyes']="True"
dnfconfig['main']['keepcache']="True"
#write the new changes to dnf.conf
with open(dnfconfig_path, 'w') as configfile:
    dnfconfig.write(configfile)
# configuring dnf done



###
run_scripts('rpm-fusion') # it has to be done before installing anything cuz some installs depends on it
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
###======================settings=============================
#mouse acc
copy_file(
    f"{current_path}/files/50-mouse-acceleration.conf",
    "/etc/X11/xorg.conf.d/50-mouse-acceleration.conf"
    )
### files that has to be executable
execute_command('chmod +x ~/.config/scripts/*')
execute_command('chmod +x ~/.config/bspwm/*')
execute_command('chmod +x ~/bin/*')


# configure sddm
sddm_config = configparser.ConfigParser()
sddm_config.optionxform = str
sddm_config_path="/etc/sddm.conf"
sddm_config.read(sddm_config_path)
sddm_config['General']['Numlock']="on"
sddm_config['Theme']['Current']="materia-dark"
#write the new changes to sddm.conf
with open(sddm_config_path, 'w') as configfile:
    sddm_config.write(configfile)
# configuring sddm done

#scripts wait for some user input
run_scripts('oh-my-zsh')


