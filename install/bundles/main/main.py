import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path_to_src = "../../src"
sys.path.insert(0, os.path.join(current_directory,relative_path_to_src))
import utils
utils.refresh_dnf()