class Movies:

    def __init__(self):
        pass

    @classmethod
    def add_movie(cls, conn, name, rating):
        cursor = conn.cursor()
        insert = "INSERT INTO Movies(name, rating) VALUES (?, ?)"
        cursor.execute(insert, (name, rating))
        conn.commit()

    @classmethod
    def delete_movie_by_name_id(cls, conn, name_id):
        cursor = conn.cursor()
        target = "DELETE FROM Movies WHERE movies_id = ?"
        cursor.execute(target, (name_id, ))

    @classmethod
    def delete_movie_by_name(cls, conn, name):
        cursor = conn.cursor()
        target = "DELETE FROM Movies WHERE movie_name = ?"
        cursor.execute(target, (name,))

    @classmethod
    def all_movies(cls, conn):
        result = conn.cursor.execute("SELECT * FROM Movies")
        return result.fetchall()
