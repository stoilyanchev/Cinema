import sqlite3
from settings import DB_NAME, SQL_FILE

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
with open(SQL_FILE, "r") as f:
    cursor.executescript(f.read())
    conn.commit()


cursor.execute("""INSERT INTO Movies(movie_name, movie_rating)
                  VALUES ("The Call", 9.5),
                         ("American Sniper", 6.5),
                         ("Fast And Furious", 7.4),
                         ("Dumb and Dumber", 10.0) """)
conn.commit()
