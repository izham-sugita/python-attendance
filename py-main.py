#! /usr/bin/env python3

import listallfiles as lst

if __name__ == '__main__':
    print("Hello!")
    all_files  = [] #initiate list
    flatest, foldest = "", "" #initiate name string

    data_dir = "./raw/"
    filetype ="*.csv"
    target = data_dir+filetype
    print(target)

    lst.listallsorted(all_files,target)
    print("Sorted list:")
    for file in all_files:
        print(file)
    
    
    print()
    flatest = lst.latestfile(all_files,flatest)
    #print(flatest)
    
    foldest=lst.oldestfile(all_files,foldest)
    #print(foldest)

#Start processing data in each file
    print("Processing.....")

    
