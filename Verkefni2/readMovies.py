import psycopg2
import getpass
import random as r

host = 'localhost'

dbname = 'movies'
username = 'postgres'

#dbname = input('Database name: ') # 'gavi'
#username = input('User name for {}.{}: '.format(host,dbname))  # 'postgres'
pw = getpass.getpass()  # 'postgres'




conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print("Connected!\n")

moviesToBeInserted = open('testmoviesdb.dat','r')
for line in moviesToBeInserted:
    print(line)
    string = line.split('::')
    movieid = string[0].strip()
    movieTitleYear = string[1].split('(')
    movieTitle = movieTitleYear[0].strip()
    #print(movieTitleYear[1].strip('('')'))
    if movieTitleYear[1].strip('('')').isdigit(): 
        
        movieYear = movieTitleYear[1].strip('('')')
    else:
        movieYear = movieTitleYear[2].strip('('')')
   # print(string[0] + ' ' + string[1] + ' ' + string[2])
    #insert into movienames(id, name) values (string[0], string[1])
    query = "INSERT INTO movies (movie_id, title, year) VALUES (%s, %s, %s);"
    data = (movieid, movieTitle, movieYear.strip())
    cursor.execute(query, data)
    #print(data)
moviesToBeInserted.close()

conn.commit()

cursor.close()
conn.close()