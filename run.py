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
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        return letters_to_numbers
    
    def print_board(self):
        """
        Prints the board.
        """
        print("  A B C D E F G H I J")
        print("-" * 31)
        row_number = 0
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Ships:
    def __init__(self, board):
        self.board = board
        
    def create_ships(self):
        """
        Creates 5 random ships for the Computer board.
        """
        for i in range(7):
            self.x_row, self.y_column = random.randint(0, 9), random.randint(0, 9)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 9), random.randint(0, 9)
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    
    def user_input(self):
        """
        Gets the user's input of their desired row and column of the ship, and provides user friendly error messages to prevent crashes.
        """
        try:
            x_row = input("Enter the row of the ship:")
            while x_row not in "0123456789":
                print("Please select a number between 0 and 9 for a valid row.")
                x_row = input("Enter the row of the ship:")
            
            y_column = input("Enter the column letter of the ship:").upper() # Converts the letter into an uppercase
            while y_column not in "ABCDEFGHIJ":
                print("Please select a letter from A, B, C, D, E, F, G, H, I and J for a valid column.")
                y_column = input("Enter the column letter of the ship:").upper()
            return int(x_row), Boards.translate_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input!")
            return self.user_input()
    
    def count_hits(self):
        """
        Counts the number of the ships on the board that have been hit.
        """
        hits = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hits += 1
        return hits

