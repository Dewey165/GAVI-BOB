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
    cursor.execute("SELECT name FROM categories WHERE category_id = '{}'".format(itemNumber))
    categoryName = cursor.fetchall()
    cursor.execute("SELECT unit_ton, unit_cost, year FROM units WHERE category_id = '{}'".format(itemNumber))
    data = cursor.fetchall()

    categoryName = str(categoryName)
    itemOne = pd.DataFrame(data, columns=['Ton', 'Cost','Year'])
    itemOne = itemOne.set_index('Year')
    print(categoryName)
    print(itemOne)
    test = itemOne.copy()
    
    test = test.astype(float)
    test.plot(kind='bar')
    plt.show()
elif menuinput == '2':
    itemNumber1 = input('Sláðu inn númer á því sem þú vilt bera saman við: ')
    itemNumber2 = input('Sláðu inn númer á því sem þú vilt bera saman við: ')
    cursor.execute("SELECT unit_ton, year FROM units WHERE category_id = '{}'".format(itemNumber1))
    data1 = cursor.fetchall()
    cursor.execute("SELECT unit_ton, year FROM units WHERE category_id = '{}'".format(itemNumber2))
    data2 = cursor.fetchall()
    itemOne = pd.DataFrame(data1, columns=['Ton','Year'])
    itemOne = itemOne.set_index('Year')
    itemTwo = pd.DataFrame(data2, columns=['Ton', 'Year'])
    itemTwo = itemTwo.set_index('Year')

    print("heiti og hann er rauður á graphi")
    print(itemOne)
    print("heiti og hann er blár á graphi")
    print(itemTwo)

    itemOne = itemOne.astype(float)
    itemTwo = itemTwo.astype(float)
    
    plt.plot(itemOne,'r')
    plt.plot(itemTwo,'b')
    plt.show()

elif menuinput == '3':
    cursor.execute("SELECT * from categories;")
    Intro = cursor.fetchall()
    for i in Intro:
        print(i)

else:
    print('Vesen')

