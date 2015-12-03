


# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:20:52 2015

@author: Ágúst
"""
import numpy as np
import pandas as pd

settings = {}

settings['encoding'] = 'utf-8'

settings['sep'] = ';'
data = pd.read_csv('import.csv', **settings)

data.columns = ['Year', 'Type', 'TotalUnits', 'TotalTons', 'TotalCost']
UnitNumber = [int(i.split(' ', 1)[0].strip(',').strip()) for i in data.Type]
UnitName = [i.split(' ', 1)[1].strip() for i in data.Type]
#print(UnitName)
#vantar að laga þegar vörutegundir eru með mörg vörunúmer, t.d. kornvörur
#forlykkja eins og UnitNumber og appenda það við UnitNr. og nota .isdigit()
data['UnitNr.'] = pd.Series(UnitNumber, index=data.index)
data['Type'] = pd.Series(UnitName, index=data.index)
Flokkur85 = data[data['UnitNr.'] == 85]

#print(Flokkur85)
T1Sjonvorp = data[data['Type'] == 'Sjónvarpstæki']
T1Sjonvorp.set_index('Year', inplace=True)
#DeltaUnits is the difference between years in TotalUnits imported
T1Sjonvorp.insert(2,'DeltaUnits', T1Sjonvorp['TotalUnits'].diff())


T2Hljodvarpstaeki = data[data['Type'] == 'Hljóðvarpstæki']
T2Hljodvarpstaeki.set_index('Year', inplace=True)
T2Hljodvarpstaeki.insert(2,'DeltaUnits', T2Hljodvarpstaeki['TotalUnits'].diff())

#print table 1 and 2
print(T1Sjonvorp)
print(T2Hljodvarpstaeki)


#Table 3 for Hljómvarpstæki
index = pd.Series(i for i in T1Sjonvorp.Year)
columns = ['TotalSjónvörp', 'TotalHljóðvarpstæki', 'TotalUnits', 'SjonTotal%', 'HljodTotal%', 'Leading Import']
T3 = pd.DataFrame(index=index, columns=columns)
T3['TotalSjónvörp'] = pd.Series([i for i in T1Sjonvorp.TotalUnits], index=T3.index)
T3['TotalHljóðvarpstæki'] = pd.Series([i for i in T2Hljodvarpstaeki.TotalUnits], index=T3.index)
T3['TotalUnits'] = T3['TotalSjónvörp'] + T3['TotalHljóðvarpstæki']
T3['SjonTotal%'] = 100*np.round((T3['TotalSjónvörp'] / T3['TotalUnits']), 3)
T3['HljodTotal%'] = 100*np.round((T3['TotalHljóðvarpstæki'] / T3['TotalUnits']),3)
T3['Leading Import'] = np.where(T3['SjonTotal%'] > T3['HljodTotal%'], 'Sjónvarpstæki', "Hljóðvarpstæki")
#print(T3)
T3.to_csv('Table3.csv')
T4 = pd.DataFrame(index=['MaxYear', 'MaxUnits', 'MinYear', 'MinUnits','Average','1999vs2015','1999vs2015%'], columns=['Sjónvarpstæki','Hljóðvarpstæki'])