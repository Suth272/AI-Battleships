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
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        return letters_to_numbers
    
    def print_board(self):
        """
        Prints the board.
        """
        print("  A B C D E F G H I J")
        print("-" * 31)
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1
