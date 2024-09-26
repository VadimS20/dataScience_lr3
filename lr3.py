import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

textfile = open("Pogoda_Ogurtsovo.txt", 'r',encoding='utf-8')
lines=textfile.readlines()

X=np.linspace(1,365,365)
Y_1=np.zeros(365)
Y_2=np.zeros(365)

lastDay=-1
countDays=0
temp=-500.0

for i in range(len(lines)):
    line=lines[i].split()
    if(int(line[1])==1970):
        if(lastDay==-1):
            lastDay=int(line[3])
        if(int(line[3])!=lastDay):
            Y_1[countDays]=temp
            temp=float(line[5])
            countDays+=1
            lastDay=int(line[3])
        else:
            temp=max(temp,float(line[5]))

lastDay=-1
countDays=0
temp=-500.0
for i in range(len(lines)):
    line=lines[i].split()           
    if(int(line[1])==1971):
        if(lastDay==-1):
            lastDay=int(line[3])
        if(int(line[3])!=lastDay):
            Y_2[countDays]=temp
            temp=float(line[5])
            countDays+=1
            lastDay=int(line[3])
        else:
            temp=max(temp,float(line[5]))

    




plt.plot(X, Y_1)
plt.plot(X, Y_2)
plt.grid()
plt.show()