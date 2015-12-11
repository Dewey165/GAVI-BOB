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
value = 4.5
cursor.execute("SELECT m.title, ROUND(AVG(r.rating)::numeric,1) FROM movies m, ratings r WHERE m.movie_id = r.movie_id GROUP BY m.title HAVING AVG(r.rating) > {} ORDER BY m.title".format(value))

rows = cursor.fetchall()
for row in rows:
	print(row)

cursor.close()
conn.close()