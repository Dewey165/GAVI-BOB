import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#SQL queries
PSQL_fetch_one_data = "SELECT unit_ton, unit_cost, year FROM units WHERE category_id = %s"

#Connect to SQL database
host = 'localhost'
dbname = 'hop3' #Enter the name of the database
username = 'postgres'
pw = '' #'Dewey123'# enter password

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
print("Connecting to database {}.{} as {}".format(host, dbname, username))
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected!\n")

selecMenu = True

# cursor.execute("""SELECT * from categories;""")
# Intro = cursor.fetchall()
# for i in Intro:
#     print(i)
#Console
print('1. skoða einn vöruflokk')
print('2. Bera saman 2 vöruflokka')
print('3. Sjá lista yfir vöruflokka')
menuinput = input()

if menuinput == '1':
    itemNumber = input('Sláðu inn númer á því sem þú vilt skoða: ')
    print(itemNumber)
    cursor.execute("SELECT unit_ton, unit_cost, year FROM units WHERE category_id = '{}'".format(itemNumber))
    #cursor.execute(PSQL_fetch_one_data, itemNumber)
    data = cursor.fetchall()
    itemOne = pd.DataFrame(data)
    print(itemOne)
    #except:
    #    print('Error, Cannot access db')
elif menuinput == '2':
    itemNumber2 = input('Sláðu inn númer á því sem þú vilt bera saman við: ')
    try:

        cursor.execute(PSQL_fetch_one_data, itemNumber2)
        data1 = cursor.fetchall()
        itemTwo = pd.DataFrame(data1)
        print(itemTwo)
    except:
        print('Error, cant select from db')
elif menuinput == '3':
    cursor.execute("""SELECT * from categories;""")
    Intro = cursor.fetchall()
    for i in Intro:
        print(i)

# try:
#     cursor.execute(PSQL_fetch_one_data, itemNumber)
#     data = cursor.fetchall()
#     itemOne = pd.DataFrame(data)
#     print(itemOne)
# except:
#     print('Error, Cannot access db')
# if menuinput == '2':
#     itemNumber2 = input('Sláðu inn númer á því sem þú vilt bera saman við: ')
#     try:
#         cursor.execute(PSQL_fetch_one_data, itemNumber2)
#         data1 = cursor.fetchall()
#         itemTwo = pd.DataFrame(data1)
#         print(itemTwo)
#     except:
#         print('Error, cant select from db')

else:
    print('Vesen')

