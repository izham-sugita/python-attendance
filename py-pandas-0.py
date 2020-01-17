'''
Test project to use pandas for attendance list updates.
The flow of the program will be:
1) Read updated attendance csv file.
2) Load the file to a temporary DataFrame.
3) Compare with the original data list and update.
'''

import pandas as pd

data = pd.read_csv("./namelist.csv")

#not really required because reading from csv file
#already produce a DataFrame
df = pd.DataFrame(data) 

print(df)

'''
print(df.ndim)
print(df.shape)
print(df.shape[0])
print(df.shape[1])
'''

#--detect new file and print the name
import glob
import os
list_of_files = glob.glob("./raw/*.csv")
latest_file = max(list_of_files, key=os.path.getctime)
print("The latest file: ", latest_file)

#--detect oldest file and print the name
oldest_file = min(list_of_files, key=os.path.getctime)
print("The oldest file: ", oldest_file)

#s = latest_file
#print(s.replace("./raw/",""))

s = latest_file.replace("./raw/","")
newcolumn = s.replace(".csv","")
print(newcolumn)

temp = pd.read_csv(latest_file)
print(temp)
print(temp.shape[0])

print()
print(temp.get("Matrix"))

list0 = temp["Matrix"].tolist()
print(list0)
list1 = df["Matrix"].tolist()
print(list1)

#working on df; from namelist.csv
#adding new column
newlist = [0]*len(list1)
for matrix in list0:
    st = matrix
    for student in list1:
        if st == student:
            #print(st,student)
            number=list1.index(st)
            newlist[number] = 1 # att=1, sabori=0


#adding newlist[number] to df-dataframe as new column
df[newcolumn]=newlist
print(df)
df.to_csv("./updated/Weekly_Attendance.csv", index=None, header=True);
df.to_csv("./namelist.csv", index=None, header=True);
