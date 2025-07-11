import random


class Boards:
    """
    Creates boards for the User and the Computer.
    """

    def __init__(self, board):
        self.board = board

    def translate_letters_to_numbers():
        """
        Translates the column labels so the computer can read it.
        """
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        """
        Prints the board that the user guesses on.
        """
        print("  A B C D E")
        print(" -----------")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

    def create_ships(self):
        """
        Creates 5 random ships for the Computer board.
        """
        for i in range(5):
            self.x, self.y = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.x][self.y] == "X":
                self.x, self.y = random.randint(0, 4), random.randint(0, 4)
            self.board[self.x][self.y] = "X"
        return self.board

    def user_input(self):
        """
        Gets the user's input of their desired row and column of the ship,
        and provides user friendly error messages to prevent crashes.
        """
        try:
            x = input("Enter the row of the ship: ").strip()

            # Empty Row input error handling
            while not x:
                print(
                    'Error: No input entered. Please enter a row number '
                    'between 1 and 5.')
                x = input("Enter the row of the ship (1-5): ").strip()

            # Out of range row input error handling
            while x not in ('1', '2', '3', '4', '5'):
                print(
                    'Error: Not an appropriate choice, please select a '
                    'valid row between 1 and 5.'
                    )
                x = input("Enter the row of the ship: ").strip()

            y = input("Enter the column letter of the ship: ").strip().upper()

            # Empty column input error handling
            while not y:
                print(
                    "Error: No input entered. Please enter a column letter "
                    "from A to E.")
                y = input(
                    "Enter the column letter of the ship (A-E): "
                    ).strip().upper()

            # Out of range row column error handling
            while y not in ("A", "B", "C", "D", "E"):
                print(
                    'Error: Not an appropriate choice, please select a '
                    'valid column from A, B, C, D or E.'
                    )
                y = input(
                    "Enter the column letter of the ship: "
                    ).strip().upper()
            return int(x) - 1, Boards.translate_letters_to_numbers()[y]
        except (ValueError, KeyError):
            print("Invalid input")
            return self.user_input()

    def count_hits(self):
        """
        Counts the number of the ships on the board that have been hit.
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def play_game():
    """
    This function starts and loops the game till the user runs out of turns.
    """
    computer_board = Boards([[" "] * 5 for i in range(5)])
    user_board = Boards([[" "] * 5 for i in range(5)])
    Boards.create_ships(computer_board)
    turns = 10
    while turns > 0:
        Boards.print_board(user_board)
        user_x, user_y = Boards.user_input(object)

        """
    Grid checking and changing/appending.
    """
        while (user_board.board[user_x][user_y] == "O"
               or user_board.board[user_x][user_y] == "X"):
            print("You have guessed this co-ordinate already.")
            user_x, user_y = Boards.user_input(object)
        if computer_board.board[user_x][user_y] == "X":
            print("Direct hit! Enemy battleship sunk!")
            user_board.board[user_x][user_y] = "X"
        else:
            print("Miss! Select new co-ordinates and try again.")
            user_board.board[user_x][user_y] = "O"

        """
        Chceking for win/loss conditions, before reducing turns.
        """
        if user_board.count_hits() == 5:
            print("You hit all 5 battleships! You win!")
            break
        elif turns == 1:
            print("You ran out of shells. You lost!")
            Boards.print_board(user_board)
            break

        turns -= 1
        print(f"You have {turns} turns remaining.")


play_game()
