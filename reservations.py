class Reservations:

    IS_AVAILABLE_QUERY = """SELECT * FROM Reservation
                            WHERE row = ? , column = ?, projection_id = ?"""

    ADD_RESERVATION_QUERY = """INSERT INTO Reservation(
                            username, projection_id, row, column
                                VALUES (?, ?, ?, ?)"""

    GET_NUMBER_OF_USED_SEATS = """ SELECT COUNT(id) as num
                                        FROM Reservation
                                        WHERE projection_id = ?"""

    USED_SEATS_ON_EACH_PR = """ SELECT projection_id ,COUNT(id) as num
                                     FROM Reservation
                                     GROUP BY projection_id """

    CANCEL_RESERVATION_QUERY = """ DELETE FROM Reservation
                                   WHERE username = ?, projection_id = ?"""

    @classmethod
    def add_reservation(cls, conn, username, projection_id, row, column,):
        if cls.is_available(conn, row, column):
            conn.cursor.execute(cls.ADD_RESERVATION_QUERY,
                                username, projection_id, row, column)
            conn.commit()

    @classmethod
    def get_number_of_used_seats_by_proj_id(cls, conn, projection_id):
        cursor = conn.cursor()
        result = cursor.execute(
            cls.GET_NUMBER_OF_AVAILABLE_SEATS, (projection_id, ))
        return result.fetchone()

    @classmethod
    def is_available(cls, conn, row, column, projection_id):
        cursor = conn.cursor()
        result = cursor.execute(
            cls.IS_AVAILABLE_QUERY, (row, column, projection_id))
        return result.fetchone() is None

    @classmethod
    def show_used_seats_on_each_projection(cls, conn):
        cursor = conn.cursor()
        result = cursor.execute(cls.USED_SEATS_ON_EACH_PR)
        return result.fetchall()

    @classmethod
    def cancel_reservation_by_username(cls, conn, username, projection_id):
        cursor = cls.conn.cursor()
        cursor.execute(cls.CANCEL_RESERVATION_QUERY, (username, projection_id))
