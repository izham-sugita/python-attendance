import csv

with open('./namelist.csv', 'r') as f:
    reader = csv.reader(f)

    rownum=0
    for row in reader:
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                print(header[colnum],col)
                colnum +=1
        rownum +=1

    f.close()

        
