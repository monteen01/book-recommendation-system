import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute(
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    rating INTEGER
)
)

conn.commit()

books = [
    ('The Great Gatsby', 'A novel about decadence and excess', 4),
    ('To Kill a Mockingbird', 'A story about racial injustice and growing up', 5),
    ('Pride and Prejudice', 'A classic romance about societal norms', 4)
]

cursor.executemany(
INSERT INTO books (name, description, rating)
VALUES (?, ?, ?)
, books)

conn.commit()

cursor.execute("SELECT * FROM books")
print("Books:")
for book in cursor.fetchall():
    print(book)

conn.close()
