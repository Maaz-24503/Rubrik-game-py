import cmpt120image
import pygame
import numpy


def createDictionary(filename):
    '''
    takes the name of csv file as input and returns a dictionary from values 0 to 9
    '''
    f = open(filename, "r")     # opens file to read
    data = {}   # empty dictionary so that we can add data later
    i = 0
    for line in f:
        if(i>10):   # because we only need values from 0 to 9
            break
        temp = line.split(",")
        if (i != 0):
            data.update({int(temp[0]):[int(temp[1]),int(temp[2]),int(temp[3])]})
        i += 1
    return data

def getColor(data, value):
    '''
    takes dictionary with color values and value of cell as parameter and
    returns the rgb list allocated to that value
    '''
    final = [0,0,0]
    temp = data.get(abs(value))
    if(value>=0):   # for positive values we jst return value from dictionary
        final = temp
    else:   # for negative values we calculate the -ve rgb value of corresponding +ve value
        final = [255-temp[0],255-temp[1],255-temp[2]]
    return final

def createColorBoard(board,data):
    '''
    takes the gameboard and colorcoding dictionary as input and
    returns 3-d list representing the gameboard square pic
    '''
    n = len(board)  # dimensions of the board
    N = n*100   # NO. pixels in each direction
    colorboard = [[0 for x in range(N)] for y in range(N)]  # creating empty list of pixels
    # using nested for loops to edit the list of pixels to their rgb values
    for row in range (n):
        for col in range(n):
            fill_square(100*row,100*col,colorboard,getColor(data,board[row][col]))
    return colorboard

def createDiagonalboard(board,data):
    '''
    takes the gameboard and colorcoding dictionary as input and
    returns 3-d list representing the gameboard diagonal pic
    '''
    n = len(board)  # dimensions of the board
    N = n * 100   # NO. pixels in each direction
    diagonalboard = [[0 for x in range(100)] for y in range(N)]   # creating empty list of pixels
    # using a for loop to edit the list of pixels to their rgb values
    for i in range(n):
        fill_square(100*i,0,diagonalboard,getColor(data,board[i][i]))
    return diagonalboard

def fill_square(x, y, img, colour):
    '''
    fills a 100x100 pixel square starting at img[x][y] with
    the RGB colour given as a parameter

    Example: fill_square(0,0,img,[255,0,0]) would set the
    upper left 100x100 pixel square of img to the colour red
    '''
    for i in range(100):
        for j in range(100):
            img[i + x][j + y] = colour

