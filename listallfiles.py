#--detect new file and print the name
import glob
import os

def listallsorted(all_files,target):
    temp = glob.glob(target)
    temp.sort(key=os.path.getmtime)
    for i in temp:
        all_files.append(i)

    return 

def latestfile(all_files, filename):
    filename = max(all_files, key=os.path.getctime)
    return filename

def oldestfile(all_files, filename):
    filename = min(all_files, key=os.path.getctime)
    return filename


    
'''    
list_of_files = glob.glob("./raw/*.csv")
print(list_of_files)

latest_file = max(list_of_files, key=os.path.getctime)
print("The latest file: ", latest_file)

#--detect oldest file and print the name
oldest_file = min(list_of_files, key=os.path.getctime)
print("The oldest file: ", oldest_file)

s = latest_file.replace("./raw/","")
newcolumn = s.replace(".csv","")
#print(newcolumn)

for files in list_of_files:
    s = files.replace("./raw/","")
    s = s.replace(".csv","")
    print(s)


all_files = glob.glob("./raw/*.csv")
all_files.sort(key=os.path.getmtime)
print(all_files)
'''

