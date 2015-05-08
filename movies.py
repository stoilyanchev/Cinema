class Movies:

    ADD_MOVIE_QUERY = "INSERT INTO Movies(name, rating) VALUES (?, ?)"
    REMOVE_MOVIE_BY_NAME_ID_QUERY = "DELETE FROM Movies WHERE movies_id = ?"
    REMOVE_MOVIE_BY_NAME_QUERY = "DELETE FROM Movies WHERE movie_name = ?"
    ALL_MOVIES_QUERY = "SELECT movie_id, movie_name, movie_rating FROM Movies"
    GET_MOVIE_BY_ID_QUERY = "SELECT * FROM Movies WHERE movie_id = ?"

    def __init__(self, conn):
        pass

    @classmethod
    def add_movie(cls, conn, name, rating):
        cursor = conn.cursor()
        cursor.execute(cls.ADD_MOVIE_QUERY, (name, rating))
        conn.commit()

    @classmethod
    def get_movie_by_id(cls, conn, movie_id):
        cursor = conn.cursor()
        result = cursor.execute(cls.GET_MOVIE_BY_ID_QUERY, (movie_id,))
        return result.fetchone()

    @classmethod
    def delete_movie_by_name_id(cls, conn, name_id):
        cursor = conn.cursor()
        cursor.execute(cls.REMOVE_MOVIE_BY_NAME_ID_QUERY, (name_id, ))

    @classmethod
    def delete_movie_by_name(cls, conn, name):
        cursor = conn.cursor()
        cursor.execute(cls.REMOVE_MOVIE_BY_NAME_QUERY, (name,))

    @classmethod
    def all_movies(cls, conn):
        cursor = conn.cursor()
        result = cursor.execute(cls.ALL_MOVIES_QUERY)
        return result.fetchall()
