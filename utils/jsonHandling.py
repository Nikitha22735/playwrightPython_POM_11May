
import json


def jsonData(filPath):
    with open(filPath) as data:
        formattedData = json.load(data)
        return formattedData
       