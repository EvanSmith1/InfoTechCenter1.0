# Print a header for the output
print("\n**************************************\n")
print("Gasoline Branch")

# Import the necessary modules
import random  # For generating random choices
from time import sleep  # To introduce delays in the output for realism


# Function to simulate a gas level gauge reading
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly choose one of the gas levels and return it
    return random.choice(gasLevelList)


# Function to simulate selecting a random gas station
def gasStations():
    # List of possible gas station names
    listOfGasStations = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly choose one gas station from the list and return it
    return random.choice(listOfGasStations)


# Function to give alerts based on the current gas level
def gasLevelAlert():
    # Randomly determine the distance to a gas station based on gas levels
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Distance for "Low" fuel level
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)  # Distance for "Quarter Tank" fuel level

    # Get the current gas level using the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Provide alerts based on the current gas level
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Pause for 2 seconds to simulate time passing
        print("Calling Triple AAA")  # Simulate calling for roadside assistance
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)  # Simulate time taken to check GPS
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station")
        sleep(2)  # Simulate GPS check
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters of a tank full which is plenty to get to your destination.")
    else:
        print("Your gas tank is full!!!")


# Call the gasLevelAlert function to run the program
gasLevelAlert()
