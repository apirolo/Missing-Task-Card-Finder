"""
Written by Alex Pirolo

03/22/2023
"""

from os import listdir
from os.path import isfile, join
from math import floor

# NOTE: Remove any files from the folder that are not task card files!!!

def missingCardNums(filePath, *seriesMax):
    """
    

    Parameters
    ----------
    filePath : String
        The path to the folder where the Task Card files are located.
        Include a lower case 'r' before the string quotes if coppying a
        file path on Windows!
        
        ie: r'C:\\Users\...'
        
    *seriesMax : int
        The last sequence number of each series present.
        
        ie: 10027, 20234, 30012, ...

    Returns
    -------
    List of missing sequence numbers.
    

    """
    
    items = []
    
    for i in range(len(seriesMax)):
        seriesMx = seriesMax[i]
        seriesMx = seriesMx + 1
        exp = len(str(seriesMx)) - 1
        seriesMin = ((floor(seriesMx/(10**exp)))*(10**exp)) + 1
        itemsTemp = [str(x) for x in list(range(seriesMin, seriesMx))]
        items = items + itemsTemp
        
    files = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    
    present = {i for i in items if any(i in j for j in files)}
    missing = set(items) - present
    
    missing = [int(x) for x in list(missing)]
    
    missing = sorted(missing)
    
    if missing == []:
        return "All task cards present. Present Sequence Numbers: {}. Found files: {}.".format(len(items), len(files))
    else:
        outstr = "There are {} missing work cards corresponding to the following sequence numbers:".format(len(missing))
        print(outstr)
        return missing