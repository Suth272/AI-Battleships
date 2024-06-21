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
    letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,}
    return letters_to_numbers

  def print_board(self):
    """
    Prints the board that the user guesses on.
    """
    print("  A B C D E F G")
    print("  +-+-+-+-+-+-+")
    row_number = 1
    for row in self.board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
class Ships:
  """
  This class handles the placement of the ships by the computer, handles the user's inputs on their chosen co-ordinates, as well as counting the number of ships that were hit.
  """
  def __init__(self, board):
    self.board = board

  def create_ships(self):
    """
    Creates 7 random ships for the Computer board.
    """
    for i in range(5):
      self.x_row, self.y_column = random.randint(0, 6), random.randint(0, 6)
      while self.board[self.x_row][self.y_column] == "X":
        self.x_row, self.y_column = random.randint(0, 6), random.randint(0, 6)
      self.board[self.x_row][self.y_column] = "X"
    return self.board

  def user_input(self):
    """
    Gets the user's input of their desired row and column of the ship, and provides user friendly error messages to prevent crashes.
    """
    try:
      x_row = input("Enter the row of the ship: ")
      while x_row not in '1234567':
          print('Not an appropriate choice, please select a valid row')
          x_row = input("Enter the row of the ship: ")

      y_column = input("Enter the column letter of the ship: ").upper()
      while y_column not in "ABCDEFG":
          print('Not an appropriate choice, please select a valid column')
          y_column = input("Enter the column letter of the ship: ").upper()
      return int(x_row) - 1, Boards.translate_letters_to_numbers()[y_column]
    except ValueError and KeyError:
      print("Not a valid input")
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

def PlayGame():
  """
  This function starts and loops the game till the user runs out of turns.
  """ 
  computer_board = Boards([[" "] * 7 for i in range(7)])
  user_guess_board = Boards([[" "] * 7 for i in range(7)])
  Ships.create_ships(computer_board)
  turns = 10
  while turns > 0:
    Boards.print_board(user_guess_board)
    #get user input
    user_x_row, user_y_column = Ships.user_input(object)
    #check if duplicate guess
    while user_guess_board.board[user_x_row][user_y_column] == "O" or user_guess_board.board[user_x_row][user_y_column] == "X":
      print("You have guessed this co-ordinate already.")
      user_x_row, user_y_column = Ships.user_input(object)
    #check for hit or miss
    if computer_board.board[user_x_row][user_y_column] == "X":
      print("Direct hit! Enemy battleship sunk!")
      user_guess_board.board[user_x_row][user_y_column] = "X"
    else:
      print("Miss! Select new co-ordinates and try again.")
      user_guess_board.board[user_x_row][user_y_column] = "O"
    #check for win or lose
    if Ships.count_hits(user_guess_board) == 5:
      print("You hit all 5 battleships! You win!")
      break
    elif turns == 0:
        print("You ran out of shells(turns). You lost!")
        Boards.print_board(user_guess_board)
        break
    else:
      turns -= 1
      print(f"You have {turns} turns remaining.")

PlayGame()