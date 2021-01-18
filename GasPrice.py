'''
Name: Xhoi Caveli
Date: 10/28/2020
Descr: This program reads weekly gas price data and displays a monthy average
of gas price for each year.
'''
def displayOutput(date, price):
    months = ('January', 'Fabruary', 'March', 'April',
              'May', 'June', 'July', 'August',
              'September', 'October','November', 'December')

    month = ""
    year = ""
    totalPrice = 0.0
    count = 0

    for i in range(len(date)):

        if date[i][0:2] != month:
            if(i != 0):
                print(' '.rjust(10),format(months[int(month) -1], '16s'), format(totalPrice/count, '.2f').rjust(10))
            month = date[i][0:2]
            totalPrice = 0
            count = 0


        if year != date[i][-4:]:
            year = date[i][-4:]
            print()
            print("Gas price averages for ", year)
            print(' '.rjust(10),format("MONTH", '18s'), 'AVERAGE'.rjust(10))
            print(' '.rjust(10),format("=====", '18s'), '======='.rjust(10))
        count += 1
        totalPrice += price[i]


def readData(file):
    date = []
    price = []


    for line in file:
        listLine = line.split(':')
        date.append(listLine[0])
        price.append(float(listLine[1].rstrip('\n')))

    return  date, price

def main():
    fileName = input('Enter the gas data file name: ')
    try:
        file = open(fileName, 'r')
    except FileNotFoundError:
        print('File cannot be found!')
    else:
        date, price = readData(file)
        displayOutput(date, price)
main()

'''SAMPLE OUTPUT
Gas price averages for  1993
           MONTH                 AVERAGE
           =====                 =======
           April                  1.08
           May                    1.10
           June                   1.10
           July                   1.08
           August                 1.06
           September              1.05
           October                1.09
           November               1.07
           December               1.01

Gas price averages for  1994
           MONTH                 AVERAGE
           =====                 =======
           January                1.00
           Fabruary               1.01
           March                  1.01
           April                  1.03
           May                    1.05
           June                   1.08
           July                   1.11
           August                 1.15
           September              1.14
           October                1.11
           November               1.12
           December               1.13

'''