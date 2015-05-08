from settings import HALL
from movies import Movies
from reservations import Reservations
from projections import Projections


class CinemaDatabaseManger:

    GET_USED_SEATS_QUERY = """
        SELECT row,column
        FROM Projection
        WHERE projection_id = ?"""

    def __init__(self, conn):
        self.__conn = conn
        self.capacity = HALL[0] * HALL[1]

    def add_movie(self):
        return Movies.add_movie(self.__conn)

    def get_movie_by_id(self, m_id):
        return Movies.get_movie_by_id(self.__conn, m_id)

    def remove_movie_by_id(self, movie_id):
        return Movies.delete_movie_by_name_id(self.__conn, movie_id)

    def remove_movie_by_name(self, movie_name):
        return Movies.delete_movie_by_name(self.__conn, movie_name)

    def show_movies(self):
        return Movies.all_movies(self.__conn)

    def show_movie_projections(self, movie_id):
        spots_unavailable = Reservations.show_used_seats_on_each_projection(
            self.__conn)
        avail_sp = {}
        for x in spots_unavailable:
            avail_sp[x['projection_id']] = self.capacity - x['num']
        return {
            "projetions":
            Projections.show_movie_projections_by_movie_id(movie_id),
            "available_spots": avail_sp}

    def get_number_of_available_seats_by_proj_id(self, projection_id):
        used = Reservations.get_number_of_used_seats_by_proj_id(
            self.__conn, projection_id)
        if used is not None:
            return self.capacity - used['num']
        else:
            raise Exception("Projection ID not in Database")

    def can_buy_tickets_by_proj_id(self, projection_id, num_of_tickets):
        seats = self.get_number_of_available_seats_by_proj_id(projection_id)
        if seats <= num_of_tickets:
            return True
        return False

    def get_used_seats(self, projection_id):
        cursor = self.conn.cursor()
        data = cursor.execute(self.GET_USED_SEATS_QUERY, (projection_id))
        result = []
        for each in data:
            value = (each['row'], each['column'])
            result.append(value)
        return result

    def check_seats_bound(self, row, column):
        if 1 <= row <= HALL[0] and 1 <= column <= HALL[1]:
            return True
        return False

    def is_available_seat(self, row, column, pr_id):
        return Reservations.is_available(self.__conn, row, column, pr_id)

    def add_reservation(self, pr_id, row, column, username):
        if self.check_seats_bound(row, column):
            if self.is_available_seat(row, column, pr_id):
                Reservations.add_reservation(
                    self.__conn, username, pr_id, row, column)
            else:
                raise Exception("This seat is already taken")
        else:
            raise Exception("Row or column not in bound")

    def cancel_reservation(self, projection_id, username):
        Reservations.cancel_reservation(self.__conn, username, projection_id)

    def get_projection_by_id(self, pr_id):
        return Projection.get_projection_by_id(self.__conn, pr_id)

