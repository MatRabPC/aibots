from math import sqrt

'''
a. a= Scenario number (1,2 or 3)
b. b= Iteration number
c. c= Agent number
d. d= Number of collected targets by the agent
e. e= Number of steps taken by the agent at the end of iteration
f. Agent happiness: f=d/(e+1)
g. g= Maximum happiness in each iteration
h. h= Minimum happiness in each iteration
i. i= Average happiness in each iteration
j. j= Standard deviation of happiness in each iteration
k. Agent competitiveness: k=(f-h)/(g-h)
'''

text = []

def fillLine(bot, scenario, iteration):
    lineText = []
    for i in range(5):
        a = scenario
        b = iteration
        c = i
        d = getTargetsCollected(bot, 5)
        e = getSteps(bot)
        f = calculateHappiness(d, e)
        lineText.append([a, b, c, d, e, f])

    for m in range(5):
        g = maxHappiness(lineText[m])
        h = minHappiness(lineText[m])
        i = aveHappiness(lineText[m])
        j = stdHappiness(lineText[m], i)
        k = (f-h)/(g-h)





def getTargetsCollected(bot, tgtMax):
    return tgtMax - bot.tgts

def getSteps(bot):
    return bot.stepsTaken

def calculateHappiness(d, e):
    return d/(e+1)

def agentCompetitiveness(f, h, g):
    return (f-h)/(g-h)

def maxHappiness(lst):
    return max(lst[5])

def minHappiness(lst):
    return min(lst[5])

def aveHappiness(lst):
    return float(sum(lst[5])) / max(len(lst[5]), 1)

def stdHappiness(lst, mean):
    return sqrt(sum((x - mean) ** 2 for x in lst) / len(lst))



with open('csvfile.csv','wb') as file:
    for line in text:
        file.write(line)
        file.write('\n')