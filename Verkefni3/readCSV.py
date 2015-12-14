import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools


# *** SQL Queries ***
PSQL_insert_category = "INSERT INTO categories (category_id, name) VALUES (%s, %s);"
PSQL_insert_units = "INSERT INTO units " \
                    "(unit_id ,category_id, unit_ton, unit_cost, unit_total, year)" \
                    " VALUES (%s, %s, %s, %s, %s, %s);"

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
CategoryNumber = [i.split(' ', 1)[0].strip() for i in data.Vöruflokkar[1:]]
#print(CategoryNumber)

CategoryName = [i.split(' ', 1)[1].strip() for i in data.Vöruflokkar[1:]]
#print(CategoryName)

#Connect to SQL database
host = 'localhost'
dbname = 'hop3' #Enter the name of the database
username = 'postgres'
pw = 'Dewey123'# enter password

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
print("Connecting to database {}.{} as {}".format(host, dbname, username))
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected!\n")

# Done, only needs to run once..
#set each row into eachRow array
eachRow = [i for i in data[1:].iterrows()]
rowCounter = 0
unit_id_counter = 1

for category_id, category_name in zip(CategoryNumber, CategoryName):
    #print(category_id, category_name)
    data = (category_id, category_name)
    cursor.execute(PSQL_insert_category, data)
    conn.commit()
    #Insert into units table
    #Fetch each row for the SQL
    unitRow = eachRow[rowCounter][1]
    year = 1998
    elementCounter = 1
    for x in range(16):
        year += 1
        units_ton = unitRow[elementCounter]
        elementCounter += 1
        unit_cost = unitRow[elementCounter]
        elementCounter += 1
        unit_total = unitRow[elementCounter]
        elementCounter += 1
        unit_id = unit_id_counter
        unit_id_counter += 1
        units = (unit_id,category_id, units_ton, unit_cost, unit_total, year)
        cursor.execute(PSQL_insert_units, units)
        conn.commit()
    rowCounter += 1


print("SQL inserts completed!")
cursor.close()
conn.close()
