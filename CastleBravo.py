print("\n********************************\n")
print("Weather Branch\n")

# Import Libraries Here
import random  # Used for random weather selection
from time import sleep  # Used to simulate delay in output

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
        print(f"\nVRS system has been engaged, only allowing you to drive {data['speed_limit']} mph")
    else:
        # Handle weather conditions not in the dictionary (e.g., "sunny")
        print(f"The NWS is calling for {weatherAlert} skies. Drive carefully to get to your destination.")
        sleep(1)
        print("\nVRS system has been disengaged")  # No VRS system needed for clear weather

# Execute the vehicle response system
vehicleResponseSystem()
