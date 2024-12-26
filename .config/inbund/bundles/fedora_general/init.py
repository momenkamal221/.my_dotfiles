#configure dnf
import configparser

from inbund.core import run_scripts
from inbund.pkgmgr.dnf import dnf
from inbund import logger 
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

run_scripts('rpm-fusion') # it has to be done before installing anything cuz some installs depends on it

def refresh_dnf():
    dnf.clear_cache()
    dnf.database_update()

logger.loading(
    "refresh dnf",
    "refreshing dnf",
    logger.MessageLevel.IN_PROGRESS,
    lambda:refresh_dnf()
)

logger.loading(
    "dnf update",
    "dnf update",
    logger.MessageLevel.IN_PROGRESS,
    lambda:dnf.update()
)