import sqlite3

connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER CHECK(rating BETWEEN 1 AND 10),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
""")

cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO users (name) VALUES (?)",
        [
            ("Aman",),
            ("Alex",),
            ("Maria",),
            ("John",),
            ("Sara",)
        ]
    )

cursor.execute("SELECT COUNT(*) FROM movies")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO movies (title, genre) VALUES (?, ?)",
        [
            ("Inception", "Фантастика"),
            ("Interstellar", "Фантастика"),
            ("Titanic", "Мелодрама"),
            ("Avatar", "Фантастика"),
            ("The Dark Knight", "Боевик")
        ]
    )

cursor.execute("SELECT COUNT(*) FROM reviews")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)",
        [
            (1, 1, 10),
            (2, 1, 9),
            (3, 2, 8),
            (4, 2, 10),
            (5, 3, 9),
            (1, 3, 7),
            (2, 4, 8),
            (3, 4, 10),
            (4, 5, 9),
            (5, 5, 8),
            (1, 2, 9),
            (2, 3, 10)
        ]
    )

connect.commit()

print("Отзывы пользователей:")

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row[0], "-", row[1], "-", row[2])

print("\nВсе фильмы:")

cursor.execute("""
SELECT movies.title, movies.genre, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row[0], "-", row[1], "-", row[2])

cursor.execute("SELECT AVG(rating) FROM reviews")
print("\nСредняя оценка:", round(cursor.fetchone()[0], 2))

cursor.execute("SELECT MAX(rating) FROM reviews")
print("Максимальная оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MIN(rating) FROM reviews")
print("Минимальная оценка:", cursor.fetchone()[0])

connect.close()