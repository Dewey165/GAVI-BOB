import psycopg2
import getpass
import numpy as np


host = 'localhost'
dbname = 'movies'
username = 'postgres'
pw = ''

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
print("Connecting to database {}.{} as {}".format(host, dbname, username))
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected!\n")

nameofmovie = input('Please write the name of the movie for details: ')
cursor.execute("SELECT m.title, m.year, ROUND(AVG(r.rating)::numeric,1) AS Rating, g.name FROM movies m, ratings r, moviegenres mg, genres g WHERE m.movie_id = r.movie_id AND m.movie_id = mg.movie_id AND mg.genre_id = g.id AND m.title = '{}' GROUP BY m.title, m.year,g.name".format(nameofmovie))

# Do some Python things to work with the list of details

rows = cursor.fetchall()
#rows = [list(i) for i in rows]
for x in rows:
	title = x[0]
	year = x[1]
	rating = x[2]
print("Title: {}| Year: {}| Rating: {}".format(title,year,rating))

cursor.execute("SELECT g.name FROM movies m, moviegenres mg, genres g WHERE m.movie_id = mg.movie_id AND mg.genre_id = g.id AND m.title = '{}' GROUP BY g.name".format(nameofmovie))

rows = cursor.fetchall()
rows = [list(i) for i in rows]

flat = [x for sublist in rows for x in sublist]
flat = np.asarray(flat)

print("Genres of the movie are: ")
print('|'.join([str(x) for x in flat]))

# Get rating of a movie
cursor.execute("SELECT ROUND(AVG(r.rating)::numeric,1) as AvgRatings FROM ratings r, movies m WHERE m.movie_id = r.movie_id AND m.title = '{}'".format(nameofmovie))

rows = cursor.fetchall()
rows = [list(i) for i in rows]
for row in rows:
	rating = row[0]
	#print('{} has {} ratings'.format(ask4movie, rating))

query = "SELECT m.title, ROUND(AVG(r.rating)::NUMERIC,1) FROM movies m, ratings r, genres g, moviegenres mg WHERE m.movie_id = r.movie_id AND g.id = mg.genre_id AND mg.movie_id = m.movie_id AND g.name IN("
query += ", ".join(['%s'] * len(flat))
query += ')'
query += "GROUP BY m.title HAVING ROUND(AVG(r.rating)::NUMERIC,1) > {}".format(rating)
cursor.execute(query, flat)

rows = cursor.fetchall()
print("Since You liked {}, then you might like: ".format(nameofmovie))
reccomend = max(rows)
title, rating = reccomend
print("Title: {} | Ratings: {}".format(title, rating))

cursor.close()
conn.close()