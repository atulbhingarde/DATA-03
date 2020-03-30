import csv
import sys
import pandas as df
import os.path
from os import path
OutPutFile="output.txt"
with open('PyBank/Resources/budget_data.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    data = (list(csvreader))
datalength=len(data)
profit=0
loss=0
realcount=0
#maxincrease=0
#maxdrop=0
prevvalue=0
total=0
positivedelta=0
negativedelta=0
#listlen=len(datalength)
for Records in range(datalength):
    #print(str(i)+str(data[i]))
    NumOfColumns=len(data[Records])
    hh=data[Records];
    for CurrentColumn in range(NumOfColumns):
        # do not use the first line in the cvs as it is header 
        # noth columns are stings 
        if ( ( Records > 0 ) & (  CurrentColumn == 1 )) :
            
            realcount = realcount + 1 
            value=int(hh[1])
            
            total = total + value 
            if ( value > 0 ):
                profit = profit + value
            else:
                loss = loss + value
            curdelta=value-prevvalue 

            if ( curdelta > positivedelta ):
                positivedelta = curdelta
                maxmonth=hh[0]
            
            if ( curdelta < negativedelta ):
                negativedelta = curdelta    
                minmonth=hh[0]
            #remember previous value as prevevalue for all records except first record as 
            #there is no previous record for first record :( 
            prevvalue=value
print("total "+str(total))           
print("profit "+str(profit))
print("loss "+str(loss))
print("total count is "+str(realcount))
a=("("'${:.0f}'.format(positivedelta)+")")
b=("("'${:.0f}'.format(negativedelta)+")")


print("Greatest Increase in Profits: " + maxmonth+ " " + a + "\n"+ "Greatest Decrease in Profits: "+ minmonth + " " +b)

#print(" file :" +str(path.exists(OutPutFile)))
#if os.path.exists(OutPutFile) :
#    os.remove(OutPutFile)
f = open(OutPutFile, "w")
f.write("Total "+str(total)+"\n")           
f.write("Total profit "+str(profit)+"\n")
f.write("Total loss "+str(loss)+"\n")
f.write("Total count is "+str(realcount)+"\n")
f.write("Greatest Increase in Profits: " + maxmonth+ " " + a + "\n"+ "Grcat eatest Decrease in Profits: "+ minmonth + " " +b)
f.close()
