print("\n********************************\n")  # Prints a decorative separator line
print("Weather Branch\n")  # Prints a header for the weather section

# Import Libraries Here
import random  # The random module is used to make random choices, such as picking a random weather condition
from time import sleep  # The sleep function will be used to pause the program for a specified time (in seconds)

# Define a function called weather that randomly selects a weather condition from a list
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]  # A list of possible weather conditions
    weatherCondition = random.choice(weatherForecast)  # Randomly select one condition from the list
    return weatherCondition  # Return the selected weather condition

# Call the weather function and store the result in the variable 'weatherAlert'
weatherAlert = weather()

# Define the vehicleResponseSystem function to react to different weather conditions
def vehicleResponseSystem():
    # Check if the weatherAlert is "snowy"
    if weatherAlert == "snowy":
        # Print a message for snowy conditions
        print("\nThe National Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Pause the program for 1 second
        print("\nVRS system has been engaged only allowing you to drive 55 mph")  # Print the VRS speed limit for snowy weather
    # Check if the weatherAlert is "blizzard"
    elif weatherAlert == "blizzard":
        print("\nThe National Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 45 mph")
    # Check if the weatherAlert is "rainy"
    elif weatherAlert == "rainy":
        print("\nThe National Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65 mph")
    # Check if the weatherAlert is "windy"
    elif weatherAlert == "windy":
        print("\nThe National Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 70 mph")
    # Check if the weatherAlert is "icy"
    elif weatherAlert == "icy":
        print("\nThe National Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 30 mph")
    # If the weatherAlert is anything else (in this case, "sunny")
    else:
        print("The NWS is calling for", weatherAlert, "skies drive carefully to get to your destination")  # Print a general message for sunny or other conditions
        sleep(1)
        print("\nVRS system has been disengaged")  # Print that the VRS system has been turned off for clear weather

# Call the vehicleResponseSystem function to execute the logic and display the response based on the current weather condition
vehicleResponseSystem()
