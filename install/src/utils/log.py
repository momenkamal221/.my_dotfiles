import sys
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
class Log:
    def __init__(self,task_name,log_file_path="") -> None:
        self.log_file_path=log_file_path
        self.task_message_length=0
        self.is_task_in_progress=False
        self.task_name=task_name
    
    #will print in progress message
    def task_started(self,message,message_type='normal'):
        task_name=self.task_name
        if self.is_task_in_progress:return
        if message_type.lower() == "error":
            task_name_colored = f"{RED}{task_name}{RESET}"
        elif message_type.lower() == "success":
            task_name_colored = f"{GREEN}{task_name}{RESET}"
        else:
            task_name_colored = f"{YELLOW}{task_name}{RESET}"
        loading_message_colored=f"[{task_name_colored}] {message}"
        sys.stdout.write("\r")
        sys.stdout.write(loading_message_colored)
        sys.stdout.flush()
        self.task_message_length=len(loading_message_colored)
        self.is_task_in_progress=True
    
    #will remove in progress message
    def task_finished(self):
        task_message_length=self.task_message_length
        sys.stdout.write("\r")
        sys.stdout.write(" " * task_message_length)
        sys.stdout.write("\r")
        sys.stdout.flush()
        self.is_task_in_progress=False
        
    def send(self, message, message_type="normal"):
        task_name=self.task_name
        if self.is_task_in_progress:return
        log_file_path=self.log_file_path
        # message_type can be normal, error, and success
        # ANSI escape codes for colors

        if message_type.lower() == "error":
            task_colored = f"{RED}{task_name}{RESET}"
        elif message_type.lower() == "success":
            task_colored = f"{GREEN}{task_name}{RESET}"
        else:
            task_colored = f"{YELLOW}{task_name}{RESET}"
        log_entry = f"[{task_name}] [{message_type}] {message}"
        log_entry_colored = f"[{task_colored}] {message}"
        print(log_entry_colored)
        # Write the log entry to the file
        if not log_file_path == "":
            with open(log_file_path, "a") as log_file:
                log_file.write(log_entry + "\n")