import datetime
import os
import dnf
import sys
import subprocess
import shutil
def execute_command(cmd):
    return subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#__init__
current_path = os.path.dirname(os.path.realpath(__file__))
log_file_name=f"{datetime.datetime.now().strftime('%y.%m.%d-%H:%M:%S')}.log"
log_file_dir=f"{current_path}/logs/"
log_file_path=f"{log_file_dir}/{log_file_name}"
if not os.path.exists(log_file_dir):
    os.makedirs(log_file_dir)
execute_command(f"touch {log_file_path}")

def run_bash_script(bash_script_path):
    subprocess.run(['bash', bash_script_path])

def get_names(file_path):
    result = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Exclude lines starting with #
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


def log(operation, message, message_type="normal", log_file_path=""):
    # message_type can be normal, error, and success
    # ANSI escape codes for colors
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    if message_type.lower() == "error":
        operation_colored = f"{RED}{operation}{RESET}"
    elif message_type.lower() == "success":
        operation_colored = f"{GREEN}{operation}{RESET}"
    else:
        operation_colored = f"{YELLOW}{operation}{RESET}"
    log_entry = f"[{operation}] [{message_type}] {message}"
    log_entry_colored = f"[{operation_colored}] {message}"
    print(log_entry_colored)
    # Write the log entry to the file
    if not log_file_path == "":
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry + "\n")

def send_operation_started(operation_name,message,message_type='normal'):
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    if message_type.lower() == "error":
        operation_name_colored = f"{RED}{operation_name}{RESET}"
    elif message_type.lower() == "success":
        operation_name_colored = f"{GREEN}{operation_name}{RESET}"
    else:
        operation_name_colored = f"{YELLOW}{operation_name}{RESET}"
    loading_message_colored=f"[{operation_name_colored}] {message}"
    sys.stdout.write("\r")
    sys.stdout.write(loading_message_colored)
    sys.stdout.flush()
    operation_message_length=len(loading_message_colored)
    return operation_message_length
def send_operation_end(operation_message_length):
    sys.stdout.write("\r")
    sys.stdout.write(" " * operation_message_length)
    sys.stdout.write("\r")
    sys.stdout.flush()

def install_packages(*packages):
    operation = 'install'
    for package in packages:
        operation_message_length=send_operation_started(operation,f'{package}: installing...')
        # Check if the package is already installed
        if dnf.is_installed(package):
            send_operation_end(operation_message_length)
            log(operation, f"{package}: already installed.",
                "success", log_file_path)
            continue
        # Check if the package is available in dnf
        if not dnf.is_available(package):
            send_operation_end(operation_message_length)
            log(operation, f"{package}: not available.", "error", log_file_path)
            continue
        # Install the package
        is_package_installed=dnf.install(package)
        send_operation_end(operation_message_length)
        if is_package_installed:
            log(operation,f'{package}: successfully installed',"success",log_file_path)
        else:
            log(operation,f'{package}: failed to install',"error",log_file_path)
def flatpak_install(*apps):
    operation = 'flatpak install'
    for app in apps:
        operation_message_length=send_operation_started(operation,f'{app}: installing...')
        # Run the Flatpak install command
        is_app_installed=execute_command(f'flatpak install -y {app}').returncode==0 or False
        send_operation_end(operation_message_length)
        if is_app_installed:
            log(operation,f'{app}: successfully installed',"success",log_file_path)
def update_system(log_file_path=''):
    operation_message_length=send_operation_started('system update',f'updating...')
    is_system_updated=dnf.update()
    send_operation_end(operation_message_length)
    if is_system_updated:
        log('update','update completed successfully',"success",log_file_path)
    else:
        log('update','failed to update',"error",log_file_path)

def refresh_dnf():
    dnf.clear_cache()
    operation_message_length=send_operation_started('refreshing dnf',f'Please wait...')
    updates_number=dnf.check_update()
    send_operation_end(operation_message_length)
    log('update',f'Found {updates_number} updates are available',"success")

def run_scripts(*scripts):
    for script in scripts:
        log('run script',f"{script}")
        run_bash_script(f"{current_path}/scripts/{script}.sh")

def copy_file(source_path, destination_path):
    operation='copy'
    # Create the destination directory if it doesn't exist
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    # Copy the file
    try:
        shutil.copy2(source_path, destination_path)
        log(operation,f"File copied from '{source_path}' to '{destination_path}'.",'success',log_file_path)
    except Exception as e:
        log(operation,f"Error copying file: {e}",'error',log_file_path)




