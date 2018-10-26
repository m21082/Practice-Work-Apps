# Saves materials to be ordered into separate csv files per supplier
# Common suppliers listed to speed up process
# Can add lines during the day and retrieve materials to be ordered at end of day
# Can search for previous orders by job name
# Job names changed to upper case to ease search function
#
# Could also use job search to find material codes??

import csv
import os
import sys
import time
from pathlib import Path
from time import gmtime, strftime

#get current system date
date = strftime("%d/%m/%Y", gmtime())

# logs materials to order into separate csv files per supplier
def supplier():
    print ()
    print ("1) Spandex")
    print ("2) All Print Supplies")
    print ("3) Sydney Beaumont")
    print ("4) Metamark")
    supp = input("Enter a supplier number above or input a name: ")
    if supp == "1":
        supp = "Spandex"
    elif supp == "2":
        supp = "APS"
    elif supp == "3":
        supp = "SydB"
    elif supp == "4":
        supp = "Metamark"
    else:
        supp = supp
    mat_code = input("Enter material code: ")
    mat_col = input ("Enter material colour name: ")
    mat_w = input ("Enter material width: ")
    mat_l = input ("Enter material length: ")
    job_ref = input ("Enter job reference: ")

    print ("Writing data to file")
    with open(supp+'.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow([date, " ", supp, " ",mat_code, " ", mat_col, " ", mat_w, " ", mat_l, " ", job_ref.upper()])
        print ("Completed")
        print ()

# prints all orders with inputted job ref
def material_search():
    job = input (" Enter job name/ref: ")

    for file_name in os.listdir():
        if file_name.endswith(".csv"):
            print ()
            with open ((file_name), 'r') as f:
                csv_reader = csv.reader(f, delimiter=",")
                for row in csv_reader:
                    if job.upper() in row:
                        print ("".join(row))
    print ()

# prints all orders with todays date
def open_order():
    print ()
    print ("***")
    for file_name in os.listdir():
        if file_name.endswith(".csv"):
            print ()
            with open ((file_name), 'r') as f:
                csv_reader = csv.reader(f, delimiter=",")
                for row in csv_reader:
                    if date in row:
                        print ("  "+("".join(row)))
    print ()
    print ("***")

#main program script loops until exit is selected
program_run = 0
while True:
    try:
        print ()
        print ("1) Create / add to order")
        print ("2) View todays orders")
        print ("3) Find material by job name")
        print ("4) Exit")
        user_prog = int(input("Please enter a number 1-4: "))
        if user_prog in range(1,10):
            if user_prog == 1:
                supplier()
            elif user_prog == 2:
                open_order()
            elif user_prog == 3:
                material_search()
            elif user_prog == 4:
                input ("Press any key to exit ")
                program_run = 1
        else:
            continue
    except ValueError:
        print ("Please enter a number 1-4")
    if program_run == 1:
        break
    else:
        continue
