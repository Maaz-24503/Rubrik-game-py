import cmpt120image
import numpy
import pygame
import myCreateImages


def welcome():
    '''
    prints the welcome message for the user and returns whether they want to play or not in boolean
    '''
    print(" Dear player! Welcome to the \"Colourful Zero\" game")
    print(" ================================================== \n")
    print("With this system you will be able to play as many games as you want!\n")
    print("The objective of this game is to make all board rows and columns sum to 0\n")
    print("For each game:\n - you will be able to choose an initial board,")
    print(
        "- at the end of each game you will win points, and \n- you will see an image "
        "representation of the last board. "
    )
    print("Enjoy!\n\n")
    choice1 = input("Would  you like to play? (y/n): ").strip(" ").lower()
    choice = True
    # Checks if the user inputted y to play game
    if (choice1 == "y"):
        choice = True
    else:
        choice = False
    return choice


def pretty_print_board(title, list2D):
    '''
    takes title and 2d list as parameter and prints the board and title with it
    '''
    print(title + "\n")
    n = len(list2D)  # taking the dimensions of the board
    sum_row = calc_sumrow(list2D)
    sum_col = calc_sumcol(list2D)
    # using nested for loops to print the 2 dimensional board with range n+2 for axis label and
    # sum row end="" at the end of the print statement removes the invisible \n so that line does
    # not get skipped
    for row in range(n + 2):
        for col in range(n + 2):
            # column headings
            if row == 0:
                if col == 0:
                    print("{:>9}".format(""), end="")
                elif col == n + 1:
                    print("{:>8}".format("Sum"))
                else:
                    label = "Col " + str(col - 1)
                    print("{:>8}".format(label), end="")
            # sum row
            elif row == n + 1:
                if col == 0:
                    print("{:>8}".format("Sum"), end="")
                elif col == n + 1:
                    print("{:>8}".format(""))
                else:
                    print("{:>8d}".format(sum_col[col - 1]), end="")
            # board data in the middle
            else:
                if col == 0:
                    label = "Row " + str(row - 1)
                    print("{:>8}".format(label), end="")
                elif col == n + 1:
                    print("{:>8d}".format(sum_row[row - 1]))
                else:
                    print("{:>8d}".format(list2D[row - 1][col - 1]), end="")


def create_initial_board(boardID):
    '''
    takes the board number user wants to play as parameter
    and returns the 2-dimensional list representing the board
    '''

    # creating filename using input
    temp = "board" + str(boardID) + ".csv"
    filename = temp.strip(" ")
    f = open(filename, "r")  # opening the file to read it
    file_content = []  # creating empty list so that we can append lines of file to it
    for line in f:
        file_content.append(line.split(","))  # each line is being store as an element as string
        # but after splitting at commas it becomes a 2-d list with our board

    n = int(file_content[0][0].strip(" "))  # first line telling us the dimensions of the board
    board = [[0 for x in range(n)] for y in range(n)]   # these for loops create an empty nxn list
    # nested for loops to input board into our nxn list of integers
    for row in range(n):
        for col in range(n):
            board[row][col] = int(file_content[row + 1][col].strip(" "))
    return board


def is_int(st):
    '''
    this functions takes a perimeter and returns true or false depending on
    whether it is an integer or not
    '''
    if st.lstrip("-").isdigit():
        return True
    else:
        return False



def calc_sumrow(board):
    '''
    takes 2-d board list as parameter,
    calculates the sum of every row and returns a list
    '''
    n = len(board)
    sum = [0] * n
    for row in range(n):
        for col in range(n):
            sum[row] = sum[row] + board[row][col]
    return sum


def calc_sumcol(board):
    '''
    takes 2-d board list as parameter,
    calculates the sum of every column and returns a list
    '''
    n = len(board)
    sum = [0] * n
    for row in range(n):
        for col in range(n):
            sum[col] = sum[col] + board[row][col]
    return sum



def all_zero(lst):
    '''
    takes 2-D list as parameter,
    checks if the sums of all the rows and columns in the list are 0 and returns a boolean
    '''

    sumcol = calc_sumcol(lst)
    sumrow = calc_sumrow(lst)
    check = True
    for i in range(len(lst)):
        if (sumcol[i] != 0 or sumrow[i] != 0):
            check = False
    return check


# printing the welcome message for the user
check = welcome()

# Initial variables so that their scope is outside the while loop as well
game_num = 0
Total_Points = 0
games_won = 0
colorlist = myCreateImages.createDictionary("colorcoding.csv")

# while loop so that the user can play as many times as they want
while (check):
    game_num += 1  # the number of game increases by 1 everytime the loop refreshes
    print("Game number: " + str(game_num) + "\n===============")
    board_num = input("Which initial board do you want to use(1,2,3,4 or 5): ")

    # while loop as error check for input
    while (not is_int(board_num) or int(board_num) > 5 or int(board_num) < 1):
        board_num = input(
            "That is not a valid value, please re-enter \n \nWhich initial board do you want to "
            "use(1,2,3,4 or 5): ")
    board = create_initial_board(board_num)
    n = len(board)
    turns = (n * n) // 2  # calculating the number of turns the user will get for the game
    while (turns > 0):
        if (turns == (n * n) // 2):  # checking if it's the first board so that we know whether
            # to print initial board
            title = "The board is \n------------- \n\n(initial board)"
            pretty_print_board(title, board)
        else:
            title = "The board is \n-------------"
            pretty_print_board(title, board)
            if all_zero(board):  # If it is not the first turn & all sums are zero the loop breaks
                break
        print("\nTurns left: " + str(turns))
        turns -= 1  # reduce number of turns after each move
        print("User, where do you want your value? (row 99 if you want no more turns)")
        Row = input("row?  (>= 0 and <= " + str(n) + "): ")
        if (Row == 99):  # checking if the user wants to end game
            break

        # loop to check input errors
        while not is_int(Row) or (int(Row) > n - 1 or int(Row) < 0) and int(Row) != 99:
            message = "That is not a valid value, please re-enter \n row?  (>= 0 and <= "
            Row = input(message + str(n) + "):  ")
        if int(Row) == 99:
            break
        Column = input("col?  (>= 0 and <= " + str(n) + "): ")

        # loop to check input errors
        while not is_int(Column) or int(Column) > n - 1 or int(Column) < 0:
            message = "That is not a valid value, please re-enter \n col?  (>= 0 and <= "
            Column = input(message + str(n) + "): ")
        replacement = input("value (>= -9 and <= 9): ")

        # loop to check input errors
        while not is_int(replacement) or int(replacement) > 9 or int(replacement) < -9:
            replacement = input("That is not a valid value, please re-enter \n value (>= -9 and "
                                "<= 9): ")
        board[int(Row)][int(Column)] = int(replacement)

    # saving the diagonal and square image for the ending board
    squarename = ("boardimage" + str(board_num) + "-" + str(game_num) + ".jpg").strip(" ")
    diagonalname = ("diagimage" + str(board_num) + "-" + str(game_num) + ".jpg").strip(" ")
    square = myCreateImages.createColorBoard(board, colorlist)
    diagonal = myCreateImages.createDiagonalboard(board, colorlist)
    cmpt120image.saveImage(square, squarename)
    cmpt120image.saveImage(diagonal, diagonalname)

    # This condition means the user has won the game
    if all_zero(board):
        # incrementing the number of games played by 1
        games_won += 1
        Points = 10 + (2 * n)   # 10 points for all zeros ,n points for each row,
        # and n for each column
        Total_Points += Points
        print("Yey! the game is over because you won! \n\nYey! Congratulations again, user, "
              "you won this game! \nYou "
              "got " + str(Points) + " points!\n\n")
        print("And now, check the image based on the last board state!!\n")
        recheck = input("Would  you like to play another game? (y/n): ").lower()
        if recheck == "y":
            check = True
        else:
            check = False

    # this condition is entered if the game is not won
    else:

        if turns == 0:  # this condition is entered if the user has run out of turns
            print("You reached the maximum turns possible,the game is over!\n\n")
        else:   # this condition is entered if the user enters 99 for row
            print("Since you didn't want to update more digits,the game is over\n\n")
        Points = 0
        sumrow = calc_sumrow(board)
        sumcol = calc_sumcol(board)
        # in this loop, one point is awarded for each row or col that sums to 0
        for i in range(n):
            if sumrow[i] == 0:
                Points += 1
            if sumcol[i] == 0:
                Points += 1
        Total_Points += Points

        if Points != 0:     # condition entered if no points are scored
            print("So sorry, User, you lost this game! "
                  "\nBut you still got points!:  " + str(Points))
        else:       # condition entered if 
            print("So sorry, User, you lost this game! \nAnd no points either... next time!")
        print("And now, check the image based on the last board state!!\n")
        recheck = input("Would  you like to play another game? (y/n): ").lower()
        if recheck == "y":
            check = True
        else:
            check = False

# prints this when the user chooses not to play any longer
print(
    "TOTALS ALL GAMES \nTotal points user in all games:  " + str(Total_Points) + "\nTotal games "
                                                                                 "the user won:  "
                                                                                 "" + str(
        games_won) + "\n\nBye!!")
