class Projections:

    ADD_PROJECTION_QUERY = """INSERT INTO Projection(
                                    movie_id, projection_type, data, time)
                              VALUES (?, ?, ?, ?) """

    REMOVE_PROJECTION_QUERY = """DELETE FROM Projection
                                 WHERE movie_id = ?, projection_type = ?,
                                 data = ?, time = ?"""

    MOVIE_PROJECTIONS_WITHOUT_DATA_QUERY = """ SELECT * FROM Projection
                                  WHERE movie_id = ?, data = ?"""

    MOVIE_PROJECTIONS_WITH_DATA_QUERY = """ SELECT * FROM Projection
                                            WHERE movie_id = ?, data = ?
                                            ORDER BY data DESC"""

    PROJECTION_BY_ID_QUERY = "SELECT * FROM Projection WHERE id = ?"

    @classmethod
    def add_projection(cls, conn, movie_id, projection_type, data, time):
        cursor = conn.cursor()
        cursor.execute(cls.ADD_PROJECTION,
                       movie_id, projection_type, data, time)
        conn.commit()

    @classmethod
    def remove_projection(cls, conn, movie_id, projection_type, data, time):
        cursor = conn.cursor()
        cursor.execute(cls.REMOVE_PROJECTION_QUERY,
                       movie_id, projection_type, data, time)

    @classmethod
    def show_movie_projections_by_movie_id(cls, conn, movie_id, data=None):
        cursor = conn.cursor()
        if data is None:
            result = cursor.execute(cls.MOVIE_PROJECTIONS_WITHOUT_DATA_QUERY,
                                    (movie_id,))
        else:
            result = cursor.execute(cls.MOVIE_PROJECTIONS_WITH_DATA_QUERY,
                                    (movie_id, data))
        return result.fetchall()

    @classmethod
    def get_projection_by_id(cls, conn, pr_id):
        cursor = conn.cursor()
        result = cursor.execute(cls.PROJECTION_BY_ID_QUERY, (pr_id, ))
        return result.fetchone()
