import sys

sys.stderr.write('This is stderr test\n')
sys.stderr.flush()
sys.stdout.write('This is stdout test\n')

print(sys.argv)

'''
import os

curdir = os.getcwd()
print(curdir)
help(os)


exdict = {'maja':[14,'blonde'], 'zero':[22,'green'], 'noname':[19,'brown'],
          'oneechan':[18,'black']}
print(exdict)
try:
    print(exdict[14])
except KeyError:
    print(KeyError)
print(exdict['maja'])
exdict['tina'] = 20
print(exdict)
exdict['tina'] = 21
print(exdict)
del exdict['zero']
print(exdict)
print(exdict['oneechan'][1])

import csv

#comma separated variables

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    dates=[]
    colors=[]

    for row in readCSV:
        color=row[3]
        date=row[0]
        
        dates.append(date)
        colors.append(color)
        
    print(dates)
    print(colors)
    print(row)
    print(row[0])
    print(roq[0],row[1])
    try:
        whatcolor=input()
        coldex=colors.index(whatcolor.lower())
        thedate=date(colordex)
     
        print(thedate)

    # except Exception, e
    except Exception as e:
        print(e)

    print('continuing')
'''
