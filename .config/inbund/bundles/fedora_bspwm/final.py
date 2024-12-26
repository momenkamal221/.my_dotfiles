import configparser
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
