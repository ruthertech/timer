from time import sleep
import os

min = 0
sec = 0
hour = 0

while True:
    sleep(1)
    sec += 1

    if sec >= 60:
        sec = 0
        min += 1

    if min >= 60:
        min = 0
        hour += 1

    os.system( ("clear", "cls") [os.name == "nt"] ) # check if system is windows or another
    print("{}:{}:{}".format(hour, min, sec))
