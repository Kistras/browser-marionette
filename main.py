from time import time, sleep

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import WebDriverException

import _importer as importer
import config

modules = importer.get_modules()



#Creating browser
# binary = FirefoxBinary(config)
# browser = Firefox(firefox_binary = binary)
# browser.set_window_size(600, 900)

