class Projections:

    def __init__(self):
        pass

    @classmethod
    def add_projection(cls, conn, movie_id, projection_type, data, time):
        cursor = conn.cursor()
        add = """INSERT INTO Projection(movie_id, projection_type, data, time)
                 VALUES (?, ?, ?, ?) """
        cursor.execute(add, movie_id, projection_type, data, time)
        conn.commit()

    @classmethod
    def remove_projection(cls, conn, movie_id, projection_type, data, time):
        cursor = conn.cursor()
        remove = """DELETE FROM Projection
                    WHERE movie_id = ?, projection_type = ?,
                    data = ?, time = ?"""
        cursor.execute(remove, movie_id, projection_type, data, time)

