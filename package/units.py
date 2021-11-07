import json
from package.definitions import ROOT_DIR

UNITS = "data/units.json"

def getUnitsData():
    unitsFile = UNITS
    f = open(unitsFile)
    unitsData = json.load(f)
    f.close()
    return unitsData

def get_unit(decimals):
    unitsData = getUnitsData()
    for i in unitsData:
        if unitsData[i] == str(10**decimals):
            return i # there are multiple units with the same value but we don't care
    return None