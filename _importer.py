from importlib import invalidate_caches
from importlib.util import find_spec, module_from_spec
from os import listdir
import sys

from _log import log

def get_modules():
    log(1, "Started importing modules.")
    modules = {} #Modules
    found_files = listdir("modules/")

    #Here path must be overridden
    prevpath = sys.path
    sys.path = [prevpath[0] + "\\modules"] #Lock for only one directory
    invalidate_caches()

    for f in found_files:
        if len(f) > 3 and f[-3:] == ".py" and f[0] != "_":
            module_name = f[:-3]
            #We will execute those modules later
            log(2, "Importing module \"%s\"."%(module_name))
            spec = find_spec(module_name)
            modules[module_name] = (spec, module_from_spec(spec))

    sys.path = prevpath #And get everything to normal so each library can use it's own dependencies

    #Each module has to be executed so it will work correctly
    for m in modules:
        log(2, "Executing module \"%s\"."%(m))
        modules[m][0].loader.exec_module(modules[m][1]) 

    log(1, "Finished importing modules.")
    return modules
