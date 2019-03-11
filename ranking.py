"""
    name: ranking.py
    author: Harsh Tagotra
    date: 12/9/2017

    This program involves processing the data and rank ordering it for a given year.
"""

from utils import *

def sorted_ranking_data(data, year):
    """
        sorts data according to given year
    :param data: given dictionaries
    :param year: given year
    :return: list
    """
    lst = []
    data1 = data[0]
    data2 = data[1]


    for i in range(len(data1['country'])):
        if year in data1 and data1[year][i]>0:
            c = CountryValue(data1['country'][i], float(data1[year][i]))
            lst.append(c)
    lst.sort(key=getValue, reverse=True)
    return lst

def getValue(i):
    return i.value

def main():
    """
        according to user given inputs, ranks data and prints top 10
    :return:
    """
    data1, data2 = read_data("worldbank_life_expectancy")
    while True:
        year = int(input("Enter year of interest (-1 to quit): "))
        if year == -1:
            break
        elif year>2015 and year<1960:
            print("Valid years are 1960-2015")
            continue
        reg = input("Enter region (type 'all' to consider all: ")
        inc = input("Enter income category: (type 'all' to consider all: ")
        if reg in data2['region'] and inc in data2['income'] or reg=='all' or inc=='all':
            fdata = filter_region((data1, data2), reg)
            fdata = filter_region(fdata, inc)
            lst = sorted_ranking_data(fdata, year)
            frontlst = lst[:10]
            backlst = lst[-10:]
            backlst = backlst[::-1]

            print("\nTop 10 life expectancies for "+str(year)+":")
            for i in range(len(frontlst)):
                print(str(i+1)+": "+str(frontlst[i].country)+" "+str(frontlst[i].value))

            print("\nBottom 10 life expectancies for "+str(year)+":")
            for i in range(len(backlst)):
                print(str(i + 1) + ": " + str(backlst[i].country) + " " + str(backlst[i].value))
        else:
            if reg not in data2['region']:
                print(reg+" is not a valid region")
            else:
                print(inc+" is not a valid income category")


if __name__ =='__main__':
    main()