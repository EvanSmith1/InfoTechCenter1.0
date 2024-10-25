print("\n***********************************************\n")
print("Gasoline Branch")

import random
from time import sleep

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
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA",
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
