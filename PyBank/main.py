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

# iterate over all records 
for Records in range(datalength):
    
    # set the record length, calculate it anyway everytime, even though it is not changing
    NumOfColumns=len(data[Records])

    # get content of record in memory 
    CurrentRecord=data[Records];

    # iterate over all records

    for CurrentColumn in range(NumOfColumns):
        # do not use the first line in the cvs as it is header 
        # both columns are strings 
        # skip the first record do not use it otherwise the int function will fail for the second column which is amount

        if ( ( Records > 0 ) & (  CurrentColumn == 1 )) :
            # increase the counter of real records excluding the first line that is header
            realcount = realcount + 1 

            # get the value of second column in current record that indicates amount could be profit or loss

            value=int(CurrentRecord[1])
            
            # increment the total by current amount 
            total = total + value 

            # if the vlaue is geater than zero then profit otherwise loss
            if ( value > 0 ):
                # this is profit
                # so increase profit :) 
                profit = profit + value
            else:
                # this is loss
                # increase loss :( 
                loss = loss + value

            # get current delta using current value and previous value
            curdelta=value-prevvalue 
            
            # if the current delta is more than positive delta in hand
            # store the current delta as psotivedelta 

            if ( curdelta > positivedelta ):
                positivedelta = curdelta
                maxmonth=CurrentRecord[0]
            
            # if the current delta i sless than the negativedelta in hand
            # store the current delta as negativedelta 

            if ( curdelta < negativedelta ):
                negativedelta = curdelta    
                minmonth=CurrentRecord[0]

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
