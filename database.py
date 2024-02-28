import sqlite3

connection = sqlite3.connect("test.db")

cursor = connection.cursor()

movies = [
    ("ted 2", "levis", 2018),
    ("Bourne", "levis", 2012),
    ("Next", "levis", 2020)
]

cursor.execute('''CREATE TABLE IF NOT EXISTS movies (title TEXT, director TEXT, year INT)''')
# inserting on row of data

# cursor.execute("INSERT INTO movies VALUES('Ted', 'Levis', 2016)")

# cursor.execute("SELECT * FROM movies")

# print(cursor.fetchone())

# inserting multiple row of data

# cursor.executemany("INSERT INTO movies VALUES (?,?,?)", movies)

# cursor.execute("SELECT title FROM movies WHERE year = 2020")

# print(cursor.fetchmany())

# Update data in the database
director_name = "dalmas"
movie_title = "Bourne"

cursor.execute("UPDATE movies SET director = ? where title = ? ", (director_name, movie_title))

cursor.execute("SELECT director FROM movies WHERE title = 'Bourne' ")

print(cursor.fetchall())

connection.commit()
connection.close()