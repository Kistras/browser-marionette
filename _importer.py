from importlib.util import find_spec, module_from_spec

def get_modules():
    modules = {} #Modules
    found_files = listdir("modules/")

    #Here path must be overridden
    prevpath = path
    path = [prevpath[0] + "\\modules"] #Lock for only one directory

    for f in found_files:
        if len(f) > 3 and f[-3:] == ".py":
            module_name = f[:-3]
            #We will execute those modules later
            spec = importlib.util.find_spec(module_name)
            modules[module_name] = (spec, importlib.util.module_from_spec(spec))

    sys.path = prevpath #And get everything to normal so each library can use it's own dependencies

    #Each module has to be executed so it will work correctly
    for m in modules:
        modules[m][0].loader.exec_module(modules[m][1]) 

    return modules