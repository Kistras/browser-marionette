import importlib
import random

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import WebDriverException

from time import time, sleep
from os import listdir
from sys import path

file_modules = listdir("modules/")
path.append(path[0]+"\\modules")
modules = {}
for fpath in file_modules:
    if fpath[-3:] != ".py": continue
    cname = fpath[:-3]
    try:
        modules[cname] = importlib.import_module(cname)
    except ValueError:
        1 #Ignore
    except:
        raise
    print(modules[cname], modules[cname].isactive(1))

#Creating browser
binary = FirefoxBinary("MFWin64/firefox.exe")
browser = Firefox(firefox_binary = binary)
browser.set_window_size(600, 900)

#Presets
currentmodule = "login"

while True:
    1

