#There's two functions that must be present in any module:
#  "defineFuncs", which will give you a function to switch modules after finishing
#     (they execute in order those funtion were called) and a function that will
#     execute other module immediately
#  "action", which will... do stuff when module is called
#You are able to just use a bit of code below and this will work probably
global switch, execute
switch = None
execute = None
def defineFuncs(switch_, execute_):
    global switch, execute
    switch = switch_
    execute = execute_

first_launch = True
def action(browser):
    

    first_launch = False
