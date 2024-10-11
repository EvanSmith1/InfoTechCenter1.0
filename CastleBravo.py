import sys
import time  # Importing required modules for system output and time delay

# ANSI escape sequences for colors
PINK = "\033[95m"
RESET = "\033[0m"  # Resets color back to default
CYAN = "\033[96m"  # Added another color for variation

# Welcome message in pink
print(f"{PINK}\nWelcome to InfoTechCenter V1.0\n{RESET}")

timeToSleep = 2 #variable to set the time library to 2 seconds when called
time.sleep(timeToSleep) # Calling the time to sleep library with the variable timeToSleeps value

X = 0  # Initialize a counter for the boot process loop
ellipsis = 0  # Initialize a counter for adding dots to the boot message

# Loop that simulates system booting
while X != 20:
    X += 1  # Increment the boot counter
    # Create a message that shows the booting process with an increasing number of dots
    message = f"{CYAN}InfoTech Center System Booting{RESET}" + "." * ellipsis
    ellipsis += 1  # Increment ellipsis counter to add another dot each iteration
    sys.stdout.write("\r" + message)  # Overwrite the same line in the console with the boot message
    sys.stdout.flush()  # Ensure the message is printed in real-time
    time.sleep(.75)  # Delay for half a second to simulate a loading process
    if ellipsis == 4:  # Reset ellipsis to 0 after 3 dots
        ellipsis = 0
    if X == 20:  # When the loop reaches 20 iterations, print the access granted message in pink
        print(f"{PINK}\n\nOperating System Booted up - Retina Scanned - Access Granted{RESET}")
