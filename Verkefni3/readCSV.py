import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Genres = [] #we do not want to hard code it
host = 'localhost'

dbname = 'movies'
username = 'postgres'

# *** SQL Queries ***

# CSV settings
settings = {}
settings['encoding'] = 'latin'
settings['sep'] = ';'
data = []

data = pd.read_csv('UTA03102.csv', **settings)
#Column names
ColumnName = [i.split(' ')[0].strip() for i in data]
data.columns = ColumnName
#Categorys number
CategoryNumber = [i.split(' ', 1)[0].strip() for i in data.Vöruflokkar]
print(CategoryNumber)
#print(data.Vöruflokkar)
CategoryName = [i.split(' ', 1)[1].strip() for i in data.Vöruflokkar[1:]]
print(CategoryName)

#UnitNumber = [int(i.split(' ', 1)[0].strip(',').strip()) for i in data.Type]
#UnitName = [i.split(' ', 1)[1].strip() for i in data.Type])
#print(data)

