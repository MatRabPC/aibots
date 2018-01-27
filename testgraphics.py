#must have graphics.py in you C:\Python27
#Info and code taken from https://stackoverflow.com/questions/15886455/simple-graphics-for-python
#base code throws an error if you "x" out of the window instead of click on the square

"""
from graphics import *
win = GraphWin(width = 200, height = 200) #Create window
win.setCoords(0,0,10,10) #set window coords
mySquare = Rectangle(Point(1,1), Point(9,9)) #create rectangle
mySquare.draw(win) #draw mySquare in the window
win.getMouse() #Pause before closing
"""

from graphics import *
#create window
win = GraphWin('MaSaAn Bots', width = 800, height = 1000) #Create window
win.setCoords(0,0,10,10) #set window coords by (x lower left, y lower left, x upper right, y upper right)
win.setBackground('black')

#create and place square border
border = Rectangle( Point(1,1), Point(9,9))
border.setOutline("white")
border.draw(win)

""" 
#create a target using circle
tgt = Circle(Point(3, 5), radius = 0.1)
tgt.setFill('white')
tgt.setOutline('red')
tgt.draw(win)
"""

#create a target using Image
tgt = Image(Point(3,5), "target.gif")
tgt.draw(win)

#create a bot
bot = Circle(Point(5, 5), radius = 0.5)
bot.setFill('blue')
bot.setOutline('white')
#bot.move(3,5)
bot.draw(win)

win.getMouse() #Pause before closing