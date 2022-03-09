# charge_readings = [1,2]
# charge_readings = [1,2]
# charge_readings = [1,2,4,6,8,9,11,12]
charge_readings = [1,2,4,10,1,2,3,4,6,8,9,11,12]

def getSortedListofUniqueItems(listOfItems):
    setofList = set(listOfItems)
    sortedList = list(setofList)
    sortedList.sort()
    
    return sortedList
    
def get_ListOfContinousRanges(charge_readings):
    listOfItems = getSortedListofUniqueItems(charge_readings)
    print(listOfItems)
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
    
    # print(listOfRange)      
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
    for item in listOfRange:
        print (f"{item['min']}-{item['max']}, {item['freq']}")
            
    
listOfRange = get_ListOfContinousRanges(charge_readings)
listOfRange = updateFreqOfRange(listOfRange,charge_readings)

output_to_console(listOfRange)
