import psycopg2
import numpy as np
import pandas as pd
import statistics
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
    
    cursor.execute("SELECT unit_ton FROM units WHERE category_id = '{}'".format(itemNumber))
    categoryTon = cursor.fetchall()
    avgTons = float(np.mean(categoryTon))
    print('Average tons: {0:.2f}'.format(avgTons))
    variance = float(np.std(categoryTon))
    print('Standard deviation is: {0:.2f}'.format(variance))

    list1 = categoryName
    str1 = ''.join(str(x) for x in list1).strip('()').strip(',')
    itemOne = pd.DataFrame(data, columns=['Ton', 'Cost','Year'])
    itemOne = itemOne.set_index('Year')
    print('Flokkurinn heitir: {}'.format(str1))
    del itemOne.index.name

    print(itemOne)
    test = itemOne.copy()

    test = test.astype(float)
    test.plot(kind='bar')
    
    plt.show()
elif menuinput == '2':
    itemNumber1 = input('Sláðu inn númer á því sem þú vilt bera saman við: ')
    cursor.execute("SELECT name FROM categories WHERE category_id = '{}'".format(itemNumber1))
    categoryName1 = cursor.fetchall()
    itemNumber2 = input('Sláðu inn númer á því sem þú vilt bera saman við: ')
    cursor.execute("SELECT name FROM categories WHERE category_id = '{}'".format(itemNumber2))
    categoryName2 = cursor.fetchall()
    cursor.execute("SELECT unit_ton, year FROM units WHERE category_id = '{}'".format(itemNumber1))
    data1 = cursor.fetchall()
    cursor.execute("SELECT unit_ton, year FROM units WHERE category_id = '{}'".format(itemNumber2))
    data2 = cursor.fetchall()
    itemOne = pd.DataFrame(data1, columns=['Ton','Year'])
    itemOne = itemOne.set_index('Year')
    itemTwo = pd.DataFrame(data2, columns=['Ton', 'Year'])
    itemTwo = itemTwo.set_index('Year')
    
    list1 = categoryName1
    str1 = ''.join(str(x) for x in list1).strip('()').strip(',')
    print('Flokkurinn heitir: {} Og er rauður á grafi'.format(str1))
    print(itemOne)
    list2 = categoryName2
    str2 = ''.join(str(x) for x in list2).strip('()').strip(',')
    print('Flokkurinn heitir: {} Og er blár á grafi'.format(str2))
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

