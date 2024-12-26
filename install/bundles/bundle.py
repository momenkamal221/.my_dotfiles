import subprocess
class Bundle:
    def __init__(self,name,directory,is_optional):
        self.name=name
        self.directory=directory
        self.is_optional = is_optional

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def execute(self):
        subprocess.call(['python',"-B",f"{self.directory}/main.py"])
    