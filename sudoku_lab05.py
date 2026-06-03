# 1. Name:
#      Jackson Edwards
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      Run the sudoku program and allow the user to input a value.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was getting the board to display correctly. It wasn't
#      too difficutlt, just weird to get everything to line up properly.
# 5. How long did it take for you to complete the assignment?
#      2 hours

import json
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(filename):
    try:
    
        with open(filename, "rt") as file:
            json_data = file.read()

            dictionary_data = json.loads(json_data)
    except (FileExistsError, FileNotFoundError):
        print("File could not be found, please enter a valid file name.\n")
        return [], False

    return dictionary_data["board"], True

def save_file(filename, board):
    try:
        with open(filename, 'w') as filehandle:
            json_data = json.dumps(board)
            filehandle.write("{\"board\" : \n"+ json_data + "\n}")

    except (FileExistsError, FileNotFoundError):
        print("File not found")

def display_board(board):
    print()
    print("   A B C D E F G H I")
    for row in range(9):
        print(row + 1, end="  ")
        for column in range(9):

            if board[row][column] == 0:
                print(" ", end="")
            
            else:
                print(f"{board[row][column]}", end="")

            if column % 3 == 2 and column != 8:
                print("|", end="")

            elif column == 8:
                print()
            
            else:
                print(end=" ")

        if row % 3 == 2 and row != 8: 
            print("   -----+-----+-----")

def check_user_square(square, board):

    column_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    column = 0
    row = 0

    if len(square) > 2 or len(square) < 2:
        print("Invalid Input")
        return row, column, False
    
    elif square[0] in column_list and 0 < int(square[1]) < 10:

        column = column_list.index(square[0])

        row = int(square[1]) - 1
    
    elif square[1] in column_list and 0 < int(square[0]) < 10:

        column = column_list.index(square[1])

        row = int(square[0]) - 1
    
    else:
        print("Invalid Input")
        return row, column, False

    if check_square_availability(row, column, board):
        return row, column, True
    else:
        print("Square Already Filled")

        return row, column, False

def check_square_availability(row, column, board):

    if board[row][column] == 0:
        return True
    else:
        return False

def get_hint(row, column, board):

    taken_numbers = []

    for number in board[row]:
        if number != 0:
            taken_numbers.append(number)
    
    for i in range(9):
        if board[i][column] != 0 and board[i][column] not in taken_numbers:
            taken_numbers.append(board[i][column])

    box_left_column = column - (column % 3)

    box_top_row = row - (row % 3)

    for r in range(box_top_row, box_top_row + 3):

        for c in range(box_left_column, box_left_column + 3):

            if board[r][c] != 0 and board[r][c] not in taken_numbers:
                taken_numbers.append(board[r][c])

    taken_numbers.sort()
    possible_numbers = [1,2,3,4,5,6,7,8,9]
    hint = [1,2,3,4,5,6,7,8,9]

    for possibility in possible_numbers:
        
        if possibility in taken_numbers:
            
            hint.pop(hint.index(possibility))

    return hint

def check_user_number(row, column, number, board):

    #Checking if number is in 1-9:

    if 0 >= number or number > 9:
        print("Invalid Number\n")

        return False

    #Checking rows and columns:

    if number in board[row]:
        print(f"{number} is already in that row\n")
        return False
    
    for i in range(9):

        if number == board[i][column]:
            print(f"{number} is already in that column\n")
            return False
    
    #Checking 3x3 square:

    box_left_column = column - (column % 3)

    box_top_row = row - (row % 3)

    for r in range(box_top_row, box_top_row + 3):

        for c in range(box_left_column, box_left_column + 3):

            if number == board[r][c]:
                print(f"{number} is already in that box\n")
                return False
    
    return True
    
def edit_board(row, column, number, board):

    board[row][column] = number

def check_win(board):

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return False
    
    return True

def main():

    valid_file = False

    while not valid_file: 
        filename = input("Please enter a filename: ")

        if filename == 'q':
            return

        board, valid_file = read_file(filename)

    play_number = 0
    i = 1

    done = False

    while not done:

        play_number += 1

        valid_square = False

        while not valid_square:
            display_board(board)

            print("Specify a coordinate to edit or 'Q' to save and quit")
            square = input("> ").lower()

            if square == "q":
                filename = input("Where would you like to save your game? (include .json) ")
                save_file(filename, board)
                return
            
            else:
                row, column, valid_square = check_user_square(square, board)

        valid_number = False

        while not valid_number:  
            number_input = input(f"What number goes in {square.upper()}?(Or enter \"S\" for a hint) ").lower()

            if number_input == "q":
                return
            
            elif number_input == "s":

                hint = get_hint(row, column, board)

                print(f"The possible numbers for {square.upper()} are: {hint}")
            
            else:

                number = int(number_input)
                valid_number = check_user_number(row, column, number, board)
        
        edit_board(row, column, number, board)

        done = check_win(board)

        if play_number % 5 == 0:
            save_file(f"{filename}.InProgress.{i}.json", board)

            print(f"Board Autosaved to {filename}.InProgress.{i}.json")
            i+=1

    clear_console()

    display_board(board)

    print("Congrats, you completed the puzzle!")

    save_file(f"{filename}.Completed.json", board)

    print(f"Board Autosaved to {filename}.Completed.json")

if __name__ == "__main__":
    main()