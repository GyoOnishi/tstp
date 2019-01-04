list1 = [['a','b','c'],['d','e','f'],['g','h','i']]

import csv
with open('09-3_answer.csv','w',newline='') as f:
    w = csv.writer(f,delimiter=',')
    for i in list1:
        w.writerow(i)
