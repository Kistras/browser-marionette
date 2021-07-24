from time import time, sleep
from collections import deque

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import WebDriverException

import _importer as importer
import config
from _log import log

#Get all external modules
modules = importer.get_modules()

#Function to call "action" function from specific module
def runmodule(name, *args, **kwargs):
    log(1, "Running \"%s\" module."%name)
    ret = modules[name][1].action(browser, *args, **kwargs)
    log(1, "Finished running \"%s\" module."%name)
    return ret

queue = deque()
#Function to queue "action" function
def queuemodule(name, *args, **kwargs):
    queue.append((name, args, kwargs))

#Queue default module immediately
queuemodule(config.defaultModule)

#Send our functions to modules
for m in modules:
    modules[m][1].defineFuncs(queuemodule, runmodule)

#Creating browser
log(2, "Creating browser.")
binary = FirefoxBinary(config.firefoxPath)
browser = Firefox(firefox_binary = binary)
browser.set_window_size(*config.windowSize)

#Doing stuff
while len(queue) > 0:
    #Get module
    mod = queue.popleft()
    #Execute module
    runmodule(mod[0], *mod[1], **mod[2])

#Close browser
log(2, "Destroying browser.")
browser.quit()