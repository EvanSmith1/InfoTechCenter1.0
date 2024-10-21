print("\n**************************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Three Quarter Tank","Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    listOfGasStations = ["VP","Shell","Meijer","Sams Club","Marathon","Moblie","Speedway","Circle K"]
    return random.choice(listOfGasStations)

print(gasLevelGauge())
print(gasStations())

#def gasLevelAlert