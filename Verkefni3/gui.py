import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#SQL queries
PSQL_fetch_one_data = "SELECT unit_tons, unit_cost, year FROM units WHERE category_id = %s;"
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

cursor.execute("""SELECT * from categories;""")
Intro = cursor.fetchall()
for i in Intro:
    print(i)
#Console
type = input('Sláðu inn "1" ef þú vilt skoða eina skrá, sláðu inn 2 ef þú vilt bera saman skrár: ')

itemNumber = input('Sláðu inn númer á því sem þú vilt skoða: ')
try:
    cursor.execute(PSQL_fetch_one_data, itemNumber)
    data = cursor.fetchall()
    itemOne = pd.DataFrame(data)
    print(itemOne)
except:
    print('Error, Cannot access db')
if type == '2':
    itemNumber2 = input('Sláðu inn númer á því sem þú vilt bera saman við: ')
    try:
        cursor.execute(PSQL_fetch_one_data, itemNumber2)
        data1 = cursor.fetchall()
        itemTwo = pd.DataFrame(data1)
        print(itemTwo)
    except:
        print('Error, cant select from db')

else:
    print('Vesen')

