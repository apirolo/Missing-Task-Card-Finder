from os import listdir
from os.path import isfile, join
from math import floor

# NOTE: Remove any files from the folder that are not task card files!!!

# def missingCardNums(filePath, *seriesMax):
#     """
    

#     Parameters
#     ----------
#     filePath : String
#         The path where the Task Card files are located.
#     *seriesMax : int
#         The last sequence number of each series present.

#     Returns
#     -------
#     List of missing sequence numbers.

#     """
    

mypath = r"C:\Users\Alex\Documents\PTA Jobs\Sky  MAX 8 MSN 42827\Files(1)\MSN 42827_HM552\DFP"

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

itemList1 = [str(x) for x in list(range(10001, 10916))]
itemList2 = [str(x) for x in list(range(20001, 20096))]
itemList3 = [str(x) for x in list(range(30001, 30029))]

items = itemList1 + itemList2 + itemList3

present = {i for i in items if any(i in j for j in files)}
missing = set(items) - present

missing = [int(x) for x in list(missing)]

missing = sorted(missing)




