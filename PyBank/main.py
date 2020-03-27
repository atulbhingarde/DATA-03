import csv
import pandas as df
with open('Resources/budget_data.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
    #next(csvreader)
    data = (list(csvreader))
print("total count is "+str(len(data)))
# print(data)
#for Recs in data:
#    print(Recs)
    #for row in csvreader:
    #    print 
dfObj = df.DataFrame(data)
new_header=dfObj.iloc[0]
dfObj = dfObj[1:]
dfObj.columns = new_header
print(dfObj.head())