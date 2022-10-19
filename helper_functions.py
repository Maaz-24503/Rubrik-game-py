import numpy as np
import cmpt120image
import pygame

#
#  Final Project: Colourful Zero Game
#  Developers: Maaz Karim
#
#  Helper file - some suggested functions with
#  just brief description and indication of parameters
#  that you may want to implement
#
#  You may create different functions and name them differently
#  These are just suggestions

# you are recommended to directly include these (or other) functions 
# in your main Python program. They are here in a separate file here just 
# to provide suggestions to you

#this function prints the welcome message for the user and returns wheter they wanna play or not
def welcome():

    print( " Dear player! Welcome to the \"Coulourful Zero\" game")
    print(" ================================================== \n")
    print("With this system you will be able to play as many games as you want!\n")
    print("The objective of this game is to make all board rows and columns sum to 0\n")
    print("For each game:\n - you will be able to choose an initial board,")
    print("- at the end of each game you will win points, and \n- you will see an image representation of the last board.")
    print("Enjoy!\n\n")
    choice1 =  input("Would  you like to play? (y/n): ").strip(" ").lower()
    choice =True
    if(choice1=="y"):
        choice = True
    else:
        choice = False
    return choice
#this function prints the board and title with it
def pretty_print_board(title, list2D):
    print(title +"\n")
    n = len(list2D)
    sum_row = calc_sumrow(list2D)
    sum_col = calc_sumcol(list2D)
    for row in range(n+2):
        for col in range(n+2):
            if(row==0):
                if(col==0):
                    print("{:>9}".format(""), end="")
                elif(col==n+1):
                    print("{:>8}".format("Sum"))
                else:
                    label = "Col "+str(col-1)
                    print("{:>8}".format(label), end="")
            elif(row==n+1):
                if(col==0):
                    print("{:>8}".format("Sum"), end="")
                elif(col==n+1):
                    print("{:>8}".format(""))
                else:
                    print("{:>8d}".format(sum_col[col-1]), end="")
            else:
                if(col==0):
                    label = "Row "+str(row-1)
                    print("{:>8}".format(label), end="")
                elif(col==n+1):
                    print("{:>8d}".format(sum_row[row-1]))
                else:
                    print("{:>8d}".format(list2D[row-1][col-1]), end="")

#this function reads the boardID and converts it
#into a 2-Dimensional array representing the board
def create_initial_board(boardID):
    temp = "board"+str(boardID)+".csv"
    filename = temp.strip(" ")
    f = open(filename, "r")
    file_content = []
    for line in f:
        file_content.append(line.split(","))

    n = int(file_content[0][0].strip(" "))
    board = [[0 for x in range(n)] for y in range(n)]
    for row in range(n):
        for col in range(n):
            board[row][col] = int(file_content[row+1][col].strip(" "))
    return board

    
def is_int(st):
    if st.lstrip("-").isdigit():
        return True
    else:
       return False

#calculates the sum of every row and returns a list
def calc_sumrow(board):
    n = len(board)
    sum = [0]*n
    for row in range (n):
        for col in range(n):
            sum[row] = sum[row]+board[row][col]
    return sum

#calculates the sum of every column and returns a list
def calc_sumcol(board):
    n = len(board)
    sum = [0]*n
    for row in range (n):
        for col in range(n):
            sum[col] = sum[col]+board[row][col]
    return sum
#checks if the sums of all the rows and columns in the list are 0 and returns a boolean
def all_zero(lst):
    sumcol = calc_sumcol(lst)
    sumrow = calc_sumrow(lst)
    check = True
    for i in range(len(lst)):
        if(sumcol[i] != 0 or sumrow[i] != 0):
            check = False
    return check
    
def fill_square(x, y, img, colour):
    '''
    fills a 100x100 pixel square starting at img[x][y] with
    the RGB colour given as a parameter
    
    Example: fill_square(0,0,img,[255,0,0]) would set the 
    upper left 100x100 pixel square of img to the colour red
    '''
    for i in range(100):
        for j in range(100):
            img[i+x][j+y] = colour

    
