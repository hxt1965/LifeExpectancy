"""
    name: growth.py
    author: Harsh Tagotra
    date: 12/10/2017

    This program ranks countries by absolute growth in life
    expectancy over a specified range of years. The data may be filtered to consider only a
    particular region or income category, or combination thereof.
"""

from utils import *

def sorted_growth_data(data, year1, year2):
    """
        sorts according to most growth in given year period
    :param data: given data
    :return: list with most growth
    """
    lst=[]
    data1=data[0]
    data2=data[1]

    for i in range(len(data1['country'])):
        if (data1[year2][i]-data1[year1][i])>0:
            c = CountryValue(data1['country'][i], data1[year2][i]-data1[year1][i])
            lst.append(c)
    lst.sort(key=getValue, reverse=True)
    return lst

def getValue(i):
    return i.value

def main():
    """
        according to user given inputs, ranks data and prints top 10

    """
    data1, data2 = read_data("worldbank_life_expectancy")
    while True:
        year1 = int(input("Enter starting year of interest (-1 to quit): "))
        if year1==-1:
            break
        year2 = int(input("Enter ending year of interest (-1 to quit): "))
        if year1==-1 or year2==-1:
            break
        elif (year1>2015 and year1<1960) or (year2>2015 and year2<1960):
            print("Valid years are 1960-2015")
            continue
        reg = input("Enter region (type 'all' to consider all: ")
        inc = input("Enter income category: (type 'all' to consider all: ")

        if reg in data2['region'] and inc in data2['income'] or reg=='all' or inc=='all':
            fdata = filter_region((data1, data2), reg)
            fdata = filter_region(fdata, inc)
            lst = sorted_growth_data(fdata, year1, year2)
            frontlst = lst[:10]
            backlst = lst[-10:]
            backlst = backlst[::-1]

            print("\nTop 10 life expectancy growth: "+str(year1)+" to "+str(year2))
            for i in range(len(frontlst)):
                print(str(i+1)+": "+str(frontlst[i].country)+" "+str(frontlst[i].value))

            print("\nBottom 10 life expectancy growth: "+str(year1)+" to "+str(year2))
            for i in range(len(backlst)):
                print(str(i + 1) + ": " + str(backlst[i].country) + " " + str(backlst[i].value))
        else:
            if reg not in data2['region']:
                print(reg+" is not a valid region")
            else:
                print(inc+" is not a valid income category")

if __name__ =='__main__':
    main()