import pandas as pd

#Set up settings for reading in csv
settings = {}
settings['encoding'] = 'utf-8'
settings['sep'] = ';'

#Read in csv file into variable
imported = pd.read_csv('import.csv',**settings)

#Rename column names
imported.columns = ['Year','Type','TotalUnits','TotalTons','TotalCost']

#Get all Types that are imported in TotalUnits > 0
TotalUnitsImported = imported['TotalUnits']>0
#new table with no 0 in TotalUnits
getUnitsImported = imported[TotalUnitsImported]

