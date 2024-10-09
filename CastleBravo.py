import sys
import time  # Importing required modules for system output and time delay

# Welcome message
print("\nWelcome to InfoTechCenter V1.0\n")

X = 0  # Initialize a counter for the boot process loop
ellipsis = 0  # Initialize a counter for adding dots to the boot message

# Loop that simulates system booting
while X != 20:
    X += 1  # Increment the boot counter
    # Create a message that shows the booting process with an increasing number of dots
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment ellipsis counter to add another dot each iteration
    sys.stdout.write("\r" + message)  # Overwrite the same line in the console with the boot message
    time.sleep(.5)  # Delay for half a second to simulate a loading process
    if ellipsis == 4:  # Reset ellipsis to 0 after 3 dots
        ellipsis = 0
    if X == 20:  # When the loop reaches 20 iterations, print the access granted message
        print("\n\nOperating System Booted up - Retina Scanned - Access Granted")
