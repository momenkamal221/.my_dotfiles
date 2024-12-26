import os
from .bundle import Bundle

bundles_dir = os.path.dirname(os.path.abspath(__file__))
bundles = {}
bundles_names=[]
optional_bundles={}
optional_bundles_names=[]


def is_optional_bundle(bundle_name:str) -> bool:
    return bundle_name.startswith("_")

def add_optional_bundle(bundle_name:str):
    bundle=Bundle(bundle_name,f"{bundles_dir}/{bundle_name}",True)
    optional_bundles[bundle_name] = bundle
    optional_bundles_names.append(bundle_name)
    
def add_normal_bundle(bundle_name:str):
    bundle=Bundle(bundle_name,f"{bundles_dir}/{bundle_name}",False)
    bundles[bundle_name] = bundle
    bundles_names.append(bundle_name)

def add_bundle(bundle_name:str):
    #this function will fill the variables 
    # bundles
    # bundles_names
    # optional_bundles
    # optional_bundles_names
    if is_optional_bundle(bundle_name):
        add_optional_bundle(bundle_name[1:])
    else:
        add_normal_bundle(bundle_name)

def __init__():
    for bundle_name in os.listdir(bundles_dir):
        if os.path.isdir(os.path.join(bundles_dir, bundle_name)):
            if bundle_name in ["__pycache__"]:continue # incase generating bytecode files is enabled
            add_bundle(bundle_name)

__init__()



