import sys
from importlib import import_module
  
# dynamic import  
def dynamic_import(name): 
    """
        function helps import modules
    """
    return import_module(name)
