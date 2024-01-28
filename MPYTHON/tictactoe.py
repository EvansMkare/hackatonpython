# Function to print board
board = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '] ]

def display_board():
  for row in board:
    print('|'.join(row))
    print('-' * 5)
    
def get_player_move(player):
  row, col = map(int, input(f"Player {player}, enter your move (row and column, e.g., 1 2): ").split())
   
  #Check if the chosen position is valid and not already occupied
  while board[row - 1][col - 1] != ' ':
    print("Invalid move. Try again.")
    row, col = map(int, input("Enter your move (row and column): ").split())
   
  return row - 1, col - 1
  
  
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or \
           board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    return False
    
    
def play_game():
  player = 'X'
  turns = 0

  while turns < 9:
    display_board()
    row, col = get_player_move(player)
    board[row][col] = player
    turns += 1
     
     #Function to check for a Winner
    if check_winner():
      display_board()
      print(f"Player {player} wins!")
      break

    player = 'O' if player == 'X' else 'X'

  if turns == 9:
    display_board()
    print("It's a tie!")

if __name__ == "__main__":
  play_game()