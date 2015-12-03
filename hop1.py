# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:20:52 2015

@author: Ágúst
"""

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('Innflutningur-hljodvarp-vs-sjonvarp.csv'))

header = next(csv_file_object)
data = []
for row in csv_file_object:
    data.append(row)

data = np.array(data)

print(data)