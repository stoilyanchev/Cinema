from setting import HALL_LENGTH, HALL_WIDTH


class Reservations:

    def __init__(self):
        self.hall = {(x, y): 0 for x in HALL_LENGTH for y in HALL_WIDTH}

    @classmethod
    def add_reservation(cls, conn, username,projection_id, row, collumn):


