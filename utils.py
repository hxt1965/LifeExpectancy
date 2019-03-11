"""
    name: utils.py
    author: Harsh Tagotra
    date: 12/8/2017

    This program involves writing tools for reading and processing the data, as well
    as defining data structures to store the data. The other programs import and use these
    tools.
"""

from rit_lib import *

CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))
Range = struct_type("Range", (str, "country"), (int, 'year1'), (int, 'year2'),
                    (float, 'value1'), (float, 'value2'))

def read_data(filename):
    """
        reads files and stores data in two dictionaries according to
        respective keys
    :param filename: name of file
    :return: two dictionaries
    """
    data1 = dict()
    data2 = dict()

    data1['country'] = []
    data1['code'] = []
    year1 = 1960
    for i in range(56):
        data1[(year1+i)] = []

    file = open("data/"+filename+"_data.txt")
    file.readline()

    for line in file:
        lst = line.split(',')
        lst.pop()
        data1['country'] += [lst[0]]
        data1['code'] += [lst[1]]
        for i in range(56):
            data1[year1+i] += ([float(lst[i+2])] if lst[i+2]!='' else [0])


    data2['code'] = []
    data2['region'] = []
    data2['income'] = []

    file = open("data/" + filename + "_metadata.txt")
    file.readline()

    for line in file:
        lst = line.split(',')
        lst.pop()
        data2['code'] += [lst[0]]
        data2['region'] += [lst[1]]
        data2['income'] += [lst[2]]

    return data1, data2


def filter_region(data, region):
    """
        filters data according to region
    :param data: data provided in form of tuple
    :param region: region to filter
    :return: dictionaries containing data respective to given region
    """
    year1=1960
    data1 = data[0]
    data2 = data[1]
    regionLst = len(data2['region'])

    fData1 = dict()
    fData1['country'] = []
    fData1['code'] = []
    for i in range(56):
        fData1[(year1+i)] = []

    fData2 = dict()
    fData2['code'] = []
    fData2['region'] = []
    fData2['income'] = []

    if region=="all":
        for i in range(regionLst):
            if data2['region'][i]!="":
                fData1['country'] += [data1['country'][i]]
                fData1['code'] += [data1['code'][i]]
                for j in range(56):
                    fData1[year1 + j] += [data1[year1+j][i]]
                fData2['code'] += [data2['code'][i]]
                fData2['region'] += [data2['region'][i]]
                fData2['income'] += [data2['income'][i]]
    elif region in data2['region']:
        for i in range(regionLst):
            if data2['region'][i] == region:
                fData1['country'] += [data1['country'][i]]
                fData1['code'] += [data1['code'][i]]
                for j in range(56):
                    fData1[year1 + j] += [data1[year1+j][i]]
                fData2['code'] += [data2['code'][i]]
                fData2['region'] += [data2['region'][i]]
                fData2['income'] += [data2['income'][i]]
    else:
        pass

    return fData1, fData2


def filter_income(data, income):
    """
            filters data according to income
        :param data: data provided in form of tuple
        :param income: income to filter
        :return: dictionaries containing data respective to given income
        """
    year1=1960
    data1 = data[0]
    data2 = data[1]
    incomeLst = len(data2['income'])

    fData1 = dict()
    fData1['country'] = []
    fData1['code'] = []
    for i in range(56):
        fData1[(year1+i)] = []

    fData2 = dict()
    fData2['code'] = []
    fData2['region'] = []
    fData2['income'] = []

    if income == "all":
        for i in range(incomeLst):
            if data2['income'][i] != "":
                fData1['country'] += [data1['country'][i]]
                fData1['code'] += [data1['code'][i]]
                for j in range(56):
                    fData1[year1 + j] += [data1[year1+j][i]]
                fData2['code'] += [data2['code'][i]]
                fData2['region'] += [data2['region'][i]]
                fData2['income'] += [data2['income'][i]]
    elif income in data2['income']:
        for i in range(incomeLst):
            if data2['income'][i] == income:
                fData1['country'] += [data1['country'][i]]
                fData1['code'] += [data1['code'][i]]
                for j in range(56):
                    fData1[year1 + j] += [data1[year1+j][i]]
                fData2['code'] += [data2['code'][i]]
                fData2['region'] += [data2['region'][i]]
                fData2['income'] += [data2['income'][i]]
    else:
        pass

    return fData1, fData2

def main():
    """
        reads files and prints data according to hard coded or user
        provided filters
    :return: None
    """
    data1, data2 = read_data("worldbank_life_expectancy")
    regionData1, regionData2 = filter_region((data1, data2), "all")

    print("Total number of countries: "+str(len(data1['country'])))
    print("Number of countries/territories: "+str(len(regionData1['country'])))

    regData = []
    print("")
    print("Regions and their country count:")
    for i in range(len(data2['region'])):
        reg = data2['region'][i]
        if reg not in regData and reg!="":
            data3, data4 = filter_region((data1, data2), reg)
            regData.append(reg)
            print(reg+": "+str(len(data3['country'])))

    incData = []
    print("")
    print("Income categories and their country count:")
    for i in range(len(data2['income'])):
        inc = data2['income'][i]
        if inc not in incData and inc != "":
            data3, data4 = filter_income((data1, data2), inc)
            incData.append(inc)
            print(inc + ": " + str(len(data3['country'])))

    reg = input("\nEnter region name: ")
    data3, data4 = filter_region((data1, data2), reg)
    if len(data3['country'])==0:
        print("Invalid input!")
    else:
        for i in range(len(data3['country'])):
            print(data3['country'][i]+" ("+data3['code'][i]+")")

    inc = input("\nEnter income category: ")
    data3, data4 = filter_income((data1, data2), inc)
    if len(data3['country']) == 0:
        print("Invalid input!")
    else:
        for i in range(len(data3['country'])):
            print(data3['country'][i] + " (" + data3['code'][i] + ")")

    while True:
        cc = input("\nEnter name of country or code (Enter to quit): ")
        if cc=="":
            break
        elif cc in data1['country'] or cc in data1['code']:
            ind = data1['country'].index(cc) if cc in data1['country'] else data1['code'].index(cc)
            print("Data for "+cc+": ")
            for i in range(56):
                if data1[(1960+i)][ind]!=0:
                    print("Year: "+str(1960+i)+" Life expectancy: "+str(data1[(1960+i)][ind]))
        else:
            print("'"+cc+"' is not a valid country name or code")


if __name__ =='__main__':
    main()