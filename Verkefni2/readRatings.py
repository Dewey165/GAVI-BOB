import psycopg2
import getpass
import random as r

host = 'localhost'

dbname = 'movies'
username = 'postgres'
pw = 'Dewey123'
# *** SQL Queries ***
PSQL_insert_ratings = "INSERT INTO ratings (id, movie_id, user_id, rating) VALUES (%s, %s, %s, %s);"

#dbname = input('Database name: ') # 'gavi'
#username = input('User name for {}.{}: '.format(host,dbname))  # 'postgres'
#pw = getpass.getpass()  # 'postgres'
#please hardcode the password so it is easier to login

# Please change postgres to your pw

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
print("Connecting to database {}.{} as {}".format(host, dbname, username))
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected!\n")

ratingsToBeInserted = open('ratings.dat', encoding="latin")
counter = 0
for line in ratingsToBeInserted:
    #print(line)
    string = line.split('::')
    userid = string[0].strip()
    movieid = string[1].strip()
    rating = string[2].strip()
    #print(userid + ' ' + movieid + ' ' + rating)
    #timestamp = string[3].strip()

    data = (counter, movieid, userid, rating)
    cursor.execute(PSQL_insert_ratings, data)
    counter += 1
ratingsToBeInserted.close()

conn.commit()

cursor.close()
conn.close()