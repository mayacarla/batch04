#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program prints []

import turtle
m = turtle.Turtle()

moves = input("Enter turtle commands: ")

myMoves = []

for i in moves:
    i.split()
    myMoves.append(i)

for i in range(len(myMoves)):
    if myMoves[i] == 'F':
        m.forward(50)
    elif myMoves[i] == 'L':
        m.left(90)
    elif myMoves[i] == 'R':
        m.right(90)
    elif myMoves[i] == '^':
        m.penup()
    elif myMoves[i] == 'v':
        m.pendown()
    elif myMoves[i] == 'B':
        m.backward(50)
    elif myMoves[i] == 'S':
        m.stamp()
    elif myMoves[i] == 'l':
        m.left(45)
    elif myMoves[i] == 'r':
        m.right(45)
    elif myMoves[i] == 'p':
        m.pencolor(("purple"))



