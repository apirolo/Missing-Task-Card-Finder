# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:36:30 2023

@author: Alex
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
from math import floor
import sv_ttk

window = tk.Tk()
window.title("Missing DFP Task Card Finder")
window.geometry("660x660")
window.resizable(False, False)
sv_ttk.set_theme("dark")

missing = []

def getFolderPath():
    FolderPathBox.delete(0, tk.END)
    folderSelection = filedialog.askdirectory()
    FolderPathBox.insert(0, folderSelection)
    
def SearchFiles():
    
    #global Results
    global resultsStr
    items = []
    
    seriesMax = SeriesBox.get()
    seriesMax = seriesMax.split(sep=', ')
    seriesMax = [int(x) for x in list(seriesMax)]
    
    for i in range(len(seriesMax)):
        seriesMx = seriesMax[i]
        seriesMx = seriesMx + 1
        exp = len(str(seriesMx)) - 1
        seriesMin = ((floor(seriesMx/(10**exp)))*(10**exp)) + 1
        itemsTemp = [str(x) for x in list(range(seriesMin, seriesMx))]
        items = items + itemsTemp
    
    filePath = FolderPathBox.get()
    files = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    
    present = {i for i in items if any(i in j for j in files)}
    missing = set(items) - present
    
    missing = [int(x) for x in list(missing)]
    
    missing = sorted(missing)
    
    missing = [str(x) for x in list(missing)]
    
    if missing == []:
        outstr = "All task cards present. Present Sequence Numbers: {}. Found files: {}.".format(len(items), len(files))
        resultsStr = outstr
        Results.config(text = resultsStr)
        return missing
    else:
        outstr = "There are {} missing work cards corresponding to the following sequence numbers:".format(len(missing))
        resultsStr = outstr
        Results.config(text = resultsStr)
        return missing
    
def insertItems():
    ResultsList.delete(1.0, tk.END)
    for i in SearchFiles(): 
        ResultsList.insert(tk.END, i + "\n")

def delete():
    resultsStr = ""
    Results.config(text = resultsStr)
    FolderPathBox.delete(0, tk.END)
    SeriesBox.delete(0, tk.END)
    ResultsList.delete(1.0, tk.END)

FolderPath = tk.StringVar()
SeriesList = tk.StringVar()
resultsStr = ""


SubTitle = tk.Label(window, text = "Tool to find missing Task Card numbers in a folder, by Alex Pirolo")
SubTitle.pack()
FolderPathLabel = tk.Label(window, text = "Path to folder containing task card files:")
FolderPathLabel.pack()
FolderPathBox = ttk.Entry(window, textvariable=FolderPath)
FolderPathBox.pack()
FolderPathButton = ttk.Button(window,
                             text = "Choose Folder", 
                             command = getFolderPath)
FolderPathButton.pack(pady=8)
SeriesBoxLabel = tk.Label(window, text = "Enter the last Sequence Number for each Series based on most recent tally, seperated by a comma and a space.")
SeriesBoxLabel.pack()
SeriesBox = ttk.Entry(window, textvariable= SeriesList)
SeriesBox.pack()
SearchButton = ttk.Button(window,
     text = "Search Files",
     command = insertItems)
     
SearchButton.pack(pady=8)
ResultsLabel = tk.Label(window, text = "Results:")
ResultsLabel.pack()
Results = tk.Label(window, text = resultsStr)
Results.pack()
ResultsList = tk.Text(window)
ResultsList.pack()
DelButton = ttk.Button(window,
                      text = "Clear Entries",
                      command = delete)
DelButton.pack(pady=8)



window.mainloop()
# Title.pack()
# SubTitle.pack()
# FolderPathLabel.pack()
# FolderPathBox.pack()
# SeriesBoxLabel.pack()
# SeriesBox.pack()
# Button.pack()

