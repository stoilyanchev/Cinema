from cinema_db_manager import CinemaDatabaseManger


class CLI_Interface:

    def __init__(self, conn):
        self.__conn = conn
        self.__manager = CinemaDatabaseManger(conn)

    def show_movies(self):
        movies = self.__manager.show_movies()
        for m in movies:
            print(m['movie_id'], m['movie_name'], m['movie_rating'])

    def show_movie_projection(self, movie_id, data=None):
        inf = self.__manager.show_movie_projections(movie_id, data)
        for x in inf['projections']:
            pr = x['id']
            print("{}  {}  {}  :'Available seats : {}'".format(
                pr, x['data'], x['time'], x['type'],
                  self.__manager.get_number_of_available_seats_by_proj_id(pr))
                  )

    def check_for_username(self, projection_id):
        name = input("Choose username> ")
        if self.has_username(name):
            print("Already taken that.Try again!")
            return self.check_for_username(projection_id)
        return name

    def check_for_tikets(self, pr_id):
        number_of_tickets = int(input("Choose number of tickets> "))
        if self.__manager.can_buy_tickets_by_proj_id(pr_id):
            return number_of_tickets
        return self.check_for_tikets(pr_id)

    def pprint_finalization(self, pr_id, seats):
        projection = self.__manager.get_projection_by_id(pr_id)
        movie = self.__manager.get_movie_by_id(projection['movie_id'])

        print("Movie: {} : {}".format(
            movie['movie_name'], movie['movie_rating']))
        print("Date and time: {}  {}  : ({})".format(
            projection['data'], projection['time'],
            projection['projection_type']))
        print("  ".join([str(x) for x in seats]))

    def make_reservation(self):
        self.show_movies()
        movie_id = int(input("Choose a movie by number> "))
        print("Projections for movie:{}".format(movie_id))
        self.show_movie_projection(movie_id)
        pr_id = int(input("Choose projection by id> "))
        self.represent_available_seats(pr_id)
        number_of_tickets = self.check_for_tikets(pr_id)
        username = self.check_for_username(pr_id)
        i = 0
        seats = []
        while i < number_of_tickets:
            row, column = int(input("Choose seat> "))
            if self.__manager.is_available_seat(row, column, pr_id):
                value = (row, column)
                seats.append(value)
                i += 1
        confirm = input("Cofirm -type 'finalize'")
        if confirm == "finalize":
            for seat in seats:
                r, c = seat
                self.__manager.add_reservation(pr_id, row, column, username)
