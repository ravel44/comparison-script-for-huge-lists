import csv
import os 

os.chdir('/pathofyourfiles') 

with open('list1.csv', 'r') as t1, open('list2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('newFile.csv', 'w') as outFile:
    i=0
    for line in filetwo:
        i=i+1
        print('line '+ str(i))
        if line not in fileone:
            outFile.write(line)
