import sqlite3
from cli_interface import CLI_Interface
from settings import DB_NAME


def pprint_commands(commands):
    index = 1
    for x, y in commands.items():
        print(index, y[0])
        index += 1


def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cinema = CLI_Interface(conn)
    available_commands = {1: ["Show movies", cinema.show_movies],
                          2: ["Make reservation", cinema.make_reservation]
                          }
    while True:
        print("Available commands: ")
        pprint_commands(available_commands)
        command = int(input("Choose command by number: "))
        (available_commands[command])[1]()
        print()

if __name__ == '__main__':
    main()
