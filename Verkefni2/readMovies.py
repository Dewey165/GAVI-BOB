import psycopg2
import getpass
import random as r
#Genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'IMAX', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
Genres = [] #we do not want to hard code it
host = 'localhost'

dbname = 'movies'
username = 'postgres'

# *** SQL Queries ***
PSQL_insert_movies = "INSERT INTO movies (movie_id, title, year) VALUES (%s, %s, %s);"
PSQL_insert_genre = "INSERT INTO genres (id, name) VALUES (%s, %s);"
PSQL_insert_moviegenres = "INSERT INTO moviegenres (movie_id, genre_id) VALUES (%s, %s)"


#dbname = input('Database name: ') # 'gavi'
#username = input('User name for {}.{}: '.format(host,dbname))  # 'postgres'
pw = getpass.getpass()  # 'postgres'


conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print("Connected!\n")

moviesToBeInserted = open('testmoviesdb.dat','r')
''' We want to set up the database on run time not hardcoded!!!
cursor.execute("""SELECT * from genres;""")
isGenresEmpty = cursor.fetchall()
if not isGenresEmpty:
    counter = 1
    for i in Genres:
        query = "INSERT INTO genres (id, name) VALUES (%s, %s);"
        print(i)
        data = (counter, i)
        cursor.execute(query, data)
        counter += 1
'''
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

    data = (movieid, movieTitle, movieYear.strip())
    cursor.execute(PSQL_insert_movies, data)
    #Inserting into moviegenres
    #Here we need to commit each time since we do not know if we are making the db or not
    conn.commit()
    movieGenres = string[2].split('|')

    for i in movieGenres:
        ThisMovieGenre = i.strip('\n')
        print(ThisMovieGenre)
        #if the genre is not in the table, insert it
        #print(Genres.index(ThisMovieGenre))
        if not ThisMovieGenre in Genres:
            data = (len(Genres) + 1, ThisMovieGenre)
            cursor.execute(PSQL_insert_genre, data)
            conn.commit()
            Genres.append(ThisMovieGenre)

        dataMoviegenres = [movieid, Genres.index(ThisMovieGenre) + 1]
        cursor.execute(PSQL_insert_moviegenres, dataMoviegenres)

moviesToBeInserted.close()

conn.commit()

cursor.close()
conn.close()