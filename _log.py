import config

LOGBASIC = 1

#Log stuff
def log(level = LOGBASIC, *args):
    if level <= config.debugLevel:
        print(*args)