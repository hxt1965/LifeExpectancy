"""
    name: factors.py
    author: Harsh Tagotra
    date: 12/10/2017

    a program which will compute one measure of the effect that
    income category and geographical region have on life expectancy.
"""

from utils import *
from turtle import *

def init(t,size,x,y):
    """
        draws graph
    :param t: turtle
    :param size: size of pen
    :param x: coordinates
    :param y: coordinates
    :return: None
    """
    t.speed(20)
    t.pensize(2)
    t.pu()
    t.goto(x*size,abs(y)*size)
    t.pd()
    t.right(90)
    i=9
    while i>0:
        t.write(i * 10,align="right", font=('Ariel', size*2, 'normal'))
        t.forward(10*size)
        i-=1
    t.write(i * 10,align="right", font=('Ariel', size*2, 'normal'))
    t.left(90)
    i = 0
    while i < 12:
        t.pu()
        t.right(90)
        t.forward(4*size)
        t.write(1960+i*5, align="center", font=('Ariel', size * 2, 'normal'))
        t.backward(3*size)
        t.pd()
        t.backward(size)
        t.left(90)
        if not(i>10):
            t.forward(10 * size)
        i += 1
    t.pu()
    t.goto((x-10) * size,2 * size)
    t.write("Life", align="left", font=('Ariel', size * 2, 'bold'))
    t.goto((x-10) * size, -2 * size)
    t.write("Exp.", align="left", font=('Ariel', size * 2, 'bold'))
    t.goto(0, (y-10) * size)
    t.write("Year", align="Center", font=('Ariel', size * 2, 'bold'))
    t.pd()

def drawLegendInc(t, x, y, size):
    """
    draws legend
    :param t: turtle
    :param x: coordinates
    :param y: coordinates
    :param size: size of pen
    :return:
    """
    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.color("Blue")
    t.write("Low income", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.color("Green")
    t.write("Lower middle income", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()
    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.color("Red")
    t.write("Upper middle income", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.color("Orange")
    t.write("High income", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

def drawLegendReg(t, x, y, size):
    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.color("Blue")
    t.write("Sub-Saharan Africa", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.color("Red")
    t.write("South Asia", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.color("Green")
    t.write("Europe and Central Asia", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(100)
    t.color("Orange")
    t.write("Latin America & Caribbean", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.color("Black")
    t.write("Middle East and North Africa", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.color("Yellow")
    t.write("North America", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()

    t.goto(x * size, abs(y) * size)
    t.left(90)
    t.forward(0)
    t.right(90)
    t.forward(100)
    t.color("Purple")
    t.write("East Asia and Pacific", align="right", font=('Ariel', size * 2, 'normal'))
    t.forward(30)
    t.down()
    t.forward(60)
    t.up()


def getVal(data):
    """
        gets all medians for all years
    :param data: given filtered data
    :return: list of medians
    """
    data1 = data[0]
    data2 = data[1]

    medians = []
    for i in range(56):
        lst = []
        for j in range(len(data1['country'])):
            lst.append(data1[1960+i][j])
        lst = sorted(lst)
        l = len(lst)//2
        medians.append(lst[l])

    return medians

def plotGI(data, inc, color, size):
    """
        plots for all incomes
    :param data: data
    :param inc: income to be printed (graphing)
    """
    t = Turtle()
    data1=data[0]
    data2=data[1]

    fdata = filter_income((data1, data2), inc)
    medians = getVal(fdata)
    t.up()
    t.color(color)
    t.goto((-55)*size, medians[0])
    #done()
    t.down()
    for i in range(56):
        t.goto((-55+i*2)*size, (45 + medians[i]))

def plotGR(data, reg, color, size):
    """
            plots for all regions
        :param data: data
        :param reg: region to be printed (graphing)
        """
    t = Turtle()
    data1=data[0]
    data2=data[1]

    fdata = filter_income((data1, data2), reg)
    medians = getVal(fdata)
    t.up()
    t.color(color)
    t.goto(-55*size, medians[0])
    #done()
    t.down()
    for i in range(56):
        t.goto(55*size + 4*size, 45*size + medians[i])

def main():
    t = Turtle()
    init(t, 4, -55, -45)
    x = -55
    y = -45
    size = 4
    t.pu()

    data1, data2 = read_data("worldbank_life_expectancy")
    fdata = filter_income((data1, data2), "all")

    input("Hit enter to continue to plot graph for incomes: ")
    init(t, 4, -55, -45)
    x = -55
    y = -45
    size = 4
    t.pu()
    drawLegendInc(t, x, y, size)
    plotGI(fdata, "Low income", "Blue", 4)
    plotGI(fdata, "Lower middle income", "Green", 4)
    plotGI(fdata, "Upper middle income", "Red", 4)
    plotGI(fdata, "High income", "Orange", 4)


    input("Hit enter to continue to plot graph for regions: ")
    t.reset()

    fdata = filter_region((data1, data2), "all")
    drawLegendReg(t, x, y, size)
    plotGR(fdata, "Middle East & North Africa", "Black", 4)
    plotGR(fdata, "Europe & Central Asia", "Green", 4)
    plotGR(fdata, "North America", "Yellow", 4)
    plotGR(fdata, "Latin America & Caribbean", "Orange", 4)
    plotGR(fdata, "South Asia", "Red", 4)
    plotGR(fdata, "East Asia & Pacific", "Purple", 4)
    plotGR(fdata, "Sub-Saharan Africa", "Blue", 4)
    done()


if __name__ =='__main__':
    main()