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
    lineText = [6]
    happiness = [6]
    for i in range(1, 6):
        a = scenario
        b = iteration
        c = i
        d = getTargetsCollected(bot, 5)
        e = getSteps(bot)
        f = calculateHappiness(d, e)
        lineText.append([a, b, c, d, e])
        happiness.append(f)
        print lineText

    #print lineText[4]

    for m in range(1, 6):
        g = maxHappiness(happiness)
        h = minHappiness(happiness)
        i = aveHappiness(happiness)
        j = stdHappiness(happiness, i)
        k = (f-h)/(g-h)

        lineText[m].append([happiness[m],g, h, i, j, k])

    return lineText



def getTargetsCollected(bot, tgtMax):
    return tgtMax - bot.tgts

def getSteps(bot):
    return bot.stepsTaken

def calculateHappiness(d, e):
    return round(float(d/(e+1.0)), 4)

def agentCompetitiveness(f, h, g):
    return float((f-h)/(g-h))

def maxHappiness(lst):
    return max(lst)

def minHappiness(lst):
    return min(lst)

def aveHappiness(lst):
    return round(float(sum(lst)) / max(len(lst), 1), 4)

def stdHappiness(lst, mean):
    return round(float(sqrt(sum((x - mean) ** 2 for x in lst) / len(lst))), 4)

def writeToCSV(text):
    with open('G9_1.csv','a') as file:
        for line in text:
            file.write(str(line))
            file.write('\n')


def fullMakeandWritetoCSV(botlot, scenario, iterationNum):
    for i in range(len(botlot)):
        a = fillLine(botlot[i], scenario, iterationNum)
        print fillLine(botlot[i], scenario, iterationNum)
        writeToCSV(a)