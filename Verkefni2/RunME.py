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

value = input('Please write the ratings you want: ')
cursor.execute("SELECT m.title, ROUND(AVG(r.rating)::numeric,1) FROM movies m, ratings r WHERE m.movie_id = r.movie_id GROUP BY m.title HAVING AVG(r.rating) > {} ORDER BY m.title".format(value))

rows = cursor.fetchall()
for row in rows:
	print(row)

movieTitle = input('Write the name of movie to get Genre of movie: ')
cursor.execute("SELECT g.name FROM movies m, moviegenres mg, genres g WHERE m.movie_id = mg.movie_id AND mg.genre_id = g.id AND m.title = '{}' GROUP BY g.name".format(movieTitle))

rows = cursor.fetchall()
for row in rows:
	print(row)

cursor.close()
conn.close()