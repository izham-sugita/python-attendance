import pandas as pd

reg = pd.read_csv("namelist.csv")
sur = pd.read_csv("namelist.csv")

print(reg.columns)
print(sur.columns)

for str in reg.columns:
    if str == 'Matrix':
        email = str

#print(email)

#to list
reglist = reg[email].to_list()
surlist = sur[email].to_list()

#print(reglist); print(surlist)

regcount = len(reglist)
surcount = len(surlist)

dup = []
for n1 in reglist:
    for n2 in surlist:
        if n1 == n2:
            dup.append(n2)

#combine list reglist,surlist
for n1 in reglist:
    surlist.append(n1)

print(len(surlist))

for nd in dup:
    surlist.remove(nd)

print(len(surlist))
print(surlist)
