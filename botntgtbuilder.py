from graphics import *

def botntgtbuilder(win):

    #create a target using circle
    tgt = Circle(Point(3, 5), radius = 1)
    tgt.setFill('white')
    tgt.setOutline('red')
    tgt.draw(win)


    #create a bot
    #or, create an array of bots #nvm, arra ynot exactly working
    bots = [Circle(Point(5,5), radius = 1)] * 5

    #bots[0].setFill('blue')
    #bots[1].setFill('red')
    #bots[2].setFill('purple')
    #bots[3].setFill('cyan')
    #bots[4].setFill('green')

    for i in range(len(bots)):
        bots[i].setOutline('white')
        #bots[i].draw(win)


    bot = Circle(Point(5,5), radius = 1)
    bot.setFill('blue')
    bot.setOutline('white')
    bot.draw(win)

    return bot, tgt