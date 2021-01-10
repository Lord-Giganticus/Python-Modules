import time
def skip():
    print('module not found, skipping.')
    time.sleep(2)
try:
    from checker import checker
except:
    skip()
try:
    from error import error
except:
    skip()