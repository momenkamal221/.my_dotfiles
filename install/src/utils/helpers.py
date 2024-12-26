import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_directory)

import datetime
import dnf
from log import Log
import subprocess
import shutil
def execute_command(cmd):
    return subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#__init__
current_path = os.path.dirname(os.path.realpath(__file__))
log_file_name=f"{datetime.datetime.now().strftime('%y.%m.%d-%H:%M:%S')}.log"
log_file_dir=f"{current_path}/logs"
log_file_path=f"{log_file_dir}/{log_file_name}"
bundles_dir=f"{current_path}/bundles"
if not os.path.exists(log_file_dir):
    os.makedirs(log_file_dir)
execute_command(f"touch {log_file_path}")

def run_bash_script(bash_script_path):
    subprocess.run(['bash', bash_script_path])


def get_names(file_path):
    result = []
    commandPrefix=">>>"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Exclude lines starting with #
                if line.startswith(commandPrefix):
                    execute_command(line[len(commandPrefix):].strip())
                    continue
                    
                if not line.strip().startswith('#'):
                    # Remove comments at the end of the line
                    line_without_comment = line.split('#')[0].strip()

                    # Split the line based on spaces and tabs
                    elements = line_without_comment.split()

                    # Remove leading and trailing whitespace from each element
                    elements = [elem.strip() for elem in elements]

                    # Add non-empty elements to the result list
                    result.extend(filter(None, elements))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return result



def remove_packages(*packages):
    remove_packages_log=Log('remove',log_file_path)
    for package in packages:
        remove_packages_log.task_started(f'{package}: removeing...')
        # Check if the package is already removed
        if not dnf.is_installed(package):
            remove_packages_log.task_finished()
            remove_packages_log.send( f"{package}: already not installed.",
                "success")
            continue
        # remove the package
        is_package_removed=dnf.remove(package)
        remove_packages_log.task_finished()
        if is_package_removed:
            remove_packages_log.send(f'{package}: successfully removed',"success")
        else:
            remove_packages_log.send(f'{package}: failed to remove',"error")

def install_packages(*packages):
    for package in packages:
        install_log=Log('install',log_file_path)
        install_log.task_started(f'{package}: installing...')
        # Check if the package is already installed
        if dnf.is_installed(package):
            install_log.task_finished()
            install_log.send( f"{package}: already installed.",
                "success")
            continue
        # Check if the package is available in dnf
        if not dnf.is_available(package):
            install_log.task_finished()
            install_log.send( f"{package}: not available.", "error")
            continue
        # Install the package
        is_package_installed=dnf.install(package)
        install_log.task_finished()
        if is_package_installed:
            install_log.send(f'{package}: successfully installed',"success")
        else:
            install_log.send(f'{package}: failed to install',"error")
def flatpak_install(*apps):
    flatpak_install_log=Log('flatpak install',log_file_path)
    for app in apps:
        flatpak_install_log.task_started(f'{app}: installing...')
        # Run the Flatpak install command
        is_app_installed=execute_command(f'flatpak install -y {app}').returncode==0 or False
        flatpak_install_log.task_finished()
        if is_app_installed:
            flatpak_install_log.send(f'{app}: successfully installed',"success")
def update_system():
    update_system_log=Log('system update',log_file_path)
    update_system_log.task_started(f'updating...')
    is_system_updated=dnf.update()
    update_system_log.task_finished()
    if is_system_updated:
        update_system_log.send('update completed successfully',"success")
    else:
        update_system_log.send('failed to update',"error")

def refresh_dnf():
    refresh_dnf_log=Log('refreshing dnf',log_file_path)
    dnf.clear_cache()
    refresh_dnf_log.task_started(f'Please wait...')
    updates_number=dnf.check_update()
    refresh_dnf_log.task_finished()
    refresh_dnf_log.send(f'Found {updates_number} updates are available',"success")

def run_scripts(*scripts):
    run_scripts_log=Log('run script')
    for script in scripts:
        run_scripts_log.send(f"{script}")
        run_bash_script(f"{current_path}/scripts/{script}.sh")

def copy_file(source_path, destination_path):
    copy_file_log=Log('copy',log_file_path)
    # Create the destination directory if it doesn't exist
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    # Copy the file
    try:
        shutil.copy2(source_path, destination_path)
        copy_file_log.send(f"File copied from '{source_path}' to '{destination_path}'.",'success')
    except Exception as e:
        copy_file_log.send(f"Error copying file: {e}",'error')
