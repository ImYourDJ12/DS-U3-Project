# Devon Taylor
# DS
# U3 Project
# 11/18/24


"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""

import turtle
from random import choice

gert = turtle.Turtle()
gert.shape('turtle')

ANGLE = 25
SIZE = 9
MOVE = 90
LEVEL = 10
BCOLOR = '#702e18'
LCOLOR = choice(['red','orange','green','pink'])

def build_tree(move,size):
  if size == 0:
    return
  else:
    if size == 1:
      gert.lt(ANGLE)
      gert.color(LCOLOR)
      gert.pensize(SIZE)
      gert.forward(move)
      gert.pensize(size)
      gert.color(BCOLOR)
    else:
      gert.lt(ANGLE)
      gert.pensize(size)
      gert.forward(move)
    if LEVEL < move:
      build_tree(move-10,size-1)
    gert.up()
    gert.backward(move)
    gert.rt(ANGLE*2)
    gert.down()
    if size == 1:
      gert.color(LCOLOR)
      gert.pensize(SIZE)
      gert.forward(move)
      gert.pensize(size)
      gert.color(BCOLOR)
    else:
      gert.pensize(size)
      gert.forward(move)
    if LEVEL < move:
      build_tree(move-10,size-1)
    gert.up()
    gert.backward(move)
    gert.lt(ANGLE)
    gert.down()

def main():
  # tree base
  gert.color(BCOLOR)
  gert.lt(90)
  gert.pensize(SIZE+1)
  gert.forward(MOVE+10)

  gert.speed("fastest")

  build_tree(MOVE,SIZE)


if __name__ == ("__main__"):
  main()

turtle.mainloop()