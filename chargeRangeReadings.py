def getSortedListofUniqueItems(listOfItems):
    setofList = set(listOfItems)
    sortedList = list(setofList)
    sortedList.sort()
    
    return sortedList
    
def get_ListOfContinousRanges(charge_readings):
    listOfItems = getSortedListofUniqueItems(charge_readings)
    # print(listOfItems)
    listOfRange=[]
    rangeDict = { "min":listOfItems[0],"max":listOfItems[0],"freq":0}
    for item in listOfItems:
        if(item <= (rangeDict["max"]+1)):
            rangeDict["max"] = item  
        else:
            listOfRange.append(rangeDict.copy())
            rangeDict["min"] = item
            rangeDict["max"] = item
    
    listOfRange.append(rangeDict.copy()) # store the last items
    
    return listOfRange
    
    
def updateFrequencyOfReading(reading,listOfRange):
    for rangeItem in listOfRange:
        if(reading <= rangeItem["max"]):
            rangeItem["freq"]=rangeItem["freq"]+1
            return listOfRange
    
    return listOfRange
    
    
def updateFreqOfRange(listOfRange,charge_readings):
    for item in charge_readings:
        listOfRange = updateFrequencyOfReading(item,listOfRange)
    return listOfRange        
    
def output_to_console(listOfRange):
    responseText = ""
    for item in listOfRange:
        responseText = f"{responseText} {item['min']}-{item['max']}, {item['freq']} \n"
        # print (responseText)
    return responseText
            
def getFreqOfChargeRanges(InputList):
    charge_readings = InputList
    listOfRange = get_ListOfContinousRanges(charge_readings)
    listOfRange = updateFreqOfRange(listOfRange,charge_readings)
    responseText = output_to_console(listOfRange)
    return responseText
