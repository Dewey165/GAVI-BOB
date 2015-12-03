# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:20:52 2015

@author: Ágúst
"""

import csv as csv
import numpy as np
import pandas as pd

csv_file_object = csv.reader(open('Innflutningur-hljodvarp-vs-sjonvarp.csv'))

settings = {}

settings['encoding'] = 'utf-8'

settings['sep'] = ';'
data = pd.read_csv('import.csv', **settings)

data.columns = ['Year', 'Type', 'TotalUnits', 'TotalTons', 'TotalCost']
UnitNumber = [int(i.split(' ', 1)[0].strip(',')) for i in data.Type]
UnitName = [i.split(' ', 1)[1] for i in data.Type]
#print(UnitName)
#vantar að laga þegar vörutegundir eru með mörg vörunúmer, t.d. kornvörur
#forlykkja eins og UnitNumber og appenda það við UnitNr. og nota .isdigit()
data['UnitNr.'] = pd.Series(UnitNumber, index=data.index)
data['Type'] = pd.Series(UnitName, index=data.index)
Flokkur85 = data[data['UnitNr.'] == 85]
print(Flokkur85)
T1Sjonvorp = data[data['Type'] == ' Sjónvarpstæki'].strip()
T2Hljodvarpstaeki = data[data['Type'] == ' Hljóðvarpstæki']
print(T1Sjonvorp)
print(T2Hljodvarpstaeki)