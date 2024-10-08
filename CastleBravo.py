import sys
import time

print("\nWelcome to InfoTechCenter V1.0\n")


X = 0
ellipsis = 0

while X != 20:
    X += 1
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if X == 20:
        print("\n\nOperating System Booted up - Retina Scanned - Access Granted")