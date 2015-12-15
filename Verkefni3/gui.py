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
pw = 'Dewey123' # enter password

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
print("Connecting to database {}.{} as {}".format(host, dbname, username))
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected!\n")

#Console options
quit = 1
while quit == 1:
        #Console
    print()
    print('1: Skoða einn vöruflokk')
    print('2: Bera saman 2 vöruflokka')
    print('3: Sjá lista yfir vöruflokka')
    print('q: Til að hætta')
    menuinput = input()
    if menuinput == '1':
        itemNumber = input('Sláðu inn númer á því sem þú vilt skoða: ')

        cursor.execute("SELECT name FROM categories WHERE category_id = '{}'".format(itemNumber))
        categoryName = cursor.fetchall()

        cursor.execute("SELECT unit_ton, unit_cost, year FROM units WHERE category_id = '{}'".format(itemNumber))
        data = cursor.fetchall()

        cursor.execute("SELECT unit_ton FROM units WHERE category_id = '{}'".format(itemNumber))
        categoryTon = cursor.fetchall()
        #Calculations
        avgTons = float(np.mean(categoryTon))
        variance = float(np.std(categoryTon))

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

        print('Average tons: {0:.2f}'.format(avgTons))
        print('Standard deviation is: {0:.2f}'.format(variance))
        plt.show()
    elif menuinput == '2':
        #item number 1
        errorCheck = 1
        while errorCheck == 1:
            itemNumber1 = input('Sláðu inn númer á vöruflokki: ')
            cursor.execute("SELECT name FROM categories WHERE category_id = '{}'".format(itemNumber1))
            categoryName1 = cursor.fetchall()
            if not categoryName1:
                print('Þessi tala er ekki til á skrá!, vinsamlegast reyndu aftur síðar...')
            else:
                errorCheck = 0
                list1 = categoryName1
                str1 = ''.join(str(x) for x in list1).strip('()').strip(',')

        #item number 2
        while errorCheck == 0:
            itemNumber2 = input('Sláðu inn númer á vöruflokki sem þú vilt bera saman við {}: '.format(str1))
            cursor.execute("SELECT name FROM categories WHERE category_id = '{}'".format(itemNumber2))
            categoryName2 = cursor.fetchall()
            print(categoryName2)
            if not categoryName2:
                 print('Þessi tala er ekki til á skrá!, vinsamlegast reyndu aftur síðar...')
            else:
                errorCheck = 1
        while errorCheck == 1:
            print('Veldu úr eftirfarandi:')
            print(' 1: Tons')
            print(' 2: Cost')
            compareItemsBy = input()
            if compareItemsBy == '1':
                cursor.execute("SELECT unit_ton, year FROM units WHERE category_id = '{}'".format(itemNumber1))
                data1 = cursor.fetchall()
                cursor.execute("SELECT unit_ton, year FROM units WHERE category_id = '{}'".format(itemNumber2))
                data2 = cursor.fetchall()
                errorCheck = 0
            elif compareItemsBy == '2':
                cursor.execute("SELECT unit_cost, year FROM units WHERE category_id = '{}'".format(itemNumber1))
                data1 = cursor.fetchall()
                cursor.execute("SELECT unit_cost, year FROM units WHERE category_id = '{}'".format(itemNumber2))
                data2 = cursor.fetchall()
                errorCheck = 0
            else:
                print('Ekki rétt valið!')
        itemOne = pd.DataFrame(data1, columns=['Ton','Year'])
        itemOne = itemOne.set_index('Year')
        itemTwo = pd.DataFrame(data2, columns=['Ton','Year'])
        itemTwo = itemTwo.set_index('Year')
        del itemOne.index.name
        del itemTwo.index.name

        list2 = categoryName2
        str2 = ''.join(str(x) for x in list2).strip('()').strip(',')

        print(itemOne)
        print('\n')
        print(itemTwo)
        print('\n')
        print('Flokkurinn heitir: {} Og er rauður á grafi'.format(str1))
        print('Flokkurinn heitir: {} Og er blár á grafi'.format(str2))

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

    elif menuinput == 'q':
        quit = 0


