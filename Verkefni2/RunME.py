import psycopg2
import getpass

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
for row in rows:
	print(row)

value = input('Please write the ratings you want: ')
cursor.execute("SELECT m.title, ROUND(AVG(r.rating)::numeric,1) FROM movies m, ratings r WHERE m.movie_id = r.movie_id GROUP BY m.title HAVING AVG(r.rating) > {} ORDER BY m.title".format(value))

#Create here python code for taking select into python list/Dict for all movies abouve x rating
rows = cursor.fetchall()
for row in rows:
	print(row)

movieTitle = input('Write the name of movie to get Genre of movie: ')
cursor.execute("SELECT g.name FROM movies m, moviegenres mg, genres g WHERE m.movie_id = mg.movie_id AND mg.genre_id = g.id AND m.title = '{}' GROUP BY g.name".format(movieTitle))

#Create here python code for taking select into python list/Dict of genres of certain movie
rows = cursor.fetchall()
for row in rows:
	print(row)



cursor.close()
conn.close()