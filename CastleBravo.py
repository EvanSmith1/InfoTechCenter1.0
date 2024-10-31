import sys
import time  # Importing required modules for system output and time delay
# Import Libraries Here
import random  # Used for random weather selection
from time import sleep  # Used to simulate delay in output
import random
from time import sleep

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

print("\n****************************************************\n")
print("Weather Branch")


def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]  # List of weather conditions
    return random.choice(weatherForecast)  # Return a randomly chosen weather condition

# Call weather function and store the result in weatherAlert
weatherAlert = weather()

# Define dictionaries to map weather conditions to alarm times and VRS speed limits
weather_data = {
    "snowy": {"alarm_delay": 30, "speed_limit": 55},
    "blizzard": {"alarm_delay": 45, "speed_limit": 45},
    "rainy": {"alarm_delay": 15, "speed_limit": 65},
    "windy": {"alarm_delay": 5, "speed_limit": 70},
    "icy": {"alarm_delay": 50, "speed_limit": 30},
}

# Define the vehicle response system function
def vehicleResponseSystem():
    # Check if the weather condition exists in the weather_data dictionary
    if weatherAlert in weather_data:
        data = weather_data[weatherAlert]  # Get the corresponding alarm delay and speed limit
        print(f"\nThe National Service has updated our alarm by {data['alarm_delay']} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS system has been engaged, only allowing you to drive {data['speed_limit']} mph.")
    else:
        # Handle weather conditions not in the dictionary (e.g., "sunny")
        print(f"The NWS is calling for {weatherAlert} skies. Drive carefully to get to your destination.")
        sleep(1)
        print("\nVRS system has been disengaged.")  # No VRS system needed for clear weather

# Execute the vehicle response system
vehicleResponseSystem()


print("\n****************************************************\n")

print("Gasoline Branch\n")


# Function to simulate gas level reading
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

# Function to simulate selecting a random gas station
def gasStations():
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)

# Function to alert based on gas level
def gasLevelAlert():
    gasLevel = gasLevelGauge()

    # Distances to gas station based on gas level (more efficient handling of random values)
    distance_alerts = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }

    # Dictionary mapping gas levels to appropriate messages/actions
    gas_responses = {
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA.",
        "Low": f"Your gas tank is extremely low. The closest gas station is {gasStations()} which is {distance_alerts['Low']} miles away.",
        "Quarter Tank": f"Your gas tank is on a quarter of a tank. The closest gas station is {gasStations()} which is {distance_alerts['Quarter Tank']} miles away.",
        "Half Tank": "Your gas tank is half full, which is plenty to get to your destination.",
        "Three Quarter Tank": "Your gas tank is three quarters full, which is plenty to get to your destination.",
        "Full Tank": "Your gas tank is full!!!"
    }

    # Simulate the alert
    if gasLevel == "Empty":
        print(gas_responses[gasLevel])
        sleep(2)
    elif gasLevel in ["Low", "Quarter Tank"]:
        print(gas_responses[gasLevel])
        sleep(2)  # Simulate GPS check
    else:
        print(gas_responses[gasLevel])

# Call the function to test it
gasLevelAlert()
