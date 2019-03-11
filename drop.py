"""
    name: drop.py
    author: Harsh Tagotra
    date: 12/10/2017

    a program which identifies the 10 worst drops in life expectancy
    throughout the 1960-2015 timeframe.
"""

from utils import *

def sorted_drop_data(data):
    """
        sorts according to max drops
    :param data: given data
    :return: list of range data structs
    """
    lst = []
    data1 = data[0]
    data2 = data[1]

    for i in range(len(data1['country'])):
        drops = []
        drop = 0
        maxDrop = 0
        for j in range(1960, 2015):
            for k in range(j+1, 2016):
                if data1[j][i]-data1[k][i]>0:
                    drop = data1[k][i] - data1[j][i]
                    if drop<maxDrop:
                        maxDrop = drop
                        r = Range(data1['country'][i], j, k, float(data1[j][i]), float(data1[k][i]))
                        drops.append(r)
                    else:
                        continue
                else:
                    break
        if len(drops)>0:
            drops.sort(key=getValue)
            lst.append(drops[0])
    lst.sort(key = getValue, reverse = True)
    return lst

def getValue(i):
    return (i.value2 - i.value1)

def main():
    """
        sorts according to worst drops and prints
    :return:
    """
    data1, data2 = read_data("worldbank_life_expectancy")
    print("\nWorst life expectancy drops: 1960 to 2015")
    lst = sorted_drop_data((data1, data2))
    lst.sort(key = getValue)
    lst = lst[:10]

    #1: Rwanda from 1984 (50.78063415) to 1993 (27.07890244): -23.701731709999997
    for i in range(10):
        print(str(i+1)+": "+lst[i].country+" from "+str(lst[i].year1)+" ("+str(lst[i].value1)+") to "+str(lst[i].year2)+
              " ("+str(lst[i].value2)+"): " + str(lst[i].value1 - lst[i].value2))

if __name__ =='__main__':
    main()