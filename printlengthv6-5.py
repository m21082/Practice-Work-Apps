# scans folder containing html job output files from wide format print rip (PosterPrint)
# searches for specific string and removes all text except print length
# saves all print lengths to csv and prints total length

import os
import re
import csv

# prints list of htm files in current folder
def scan_folder(parent):
    print ("Scanning htm files")
    print("")
    try:
        os.remove("printlength.csv")
    except IOError:
        print ("")
    try:
        os.remove("printlength1.csv")
    except IOError:
        print ("")
    # iterate over all the files in directory 'parent'
    for file_name in os.listdir(parent):
        if file_name.endswith(".htm"):
            # prints length of print from htm file found
            file = open(file_name , "rt").readlines()
            #assign text to print_length in case it isn't found
            print_length = "<tr><td>Media</td><td>0.00 mm</td><td>0.00</td></tr>"
            #search each line in file for keyword "Media"
            for line_number, line in enumerate(file):
                if ">Media<" in line:
                    print (file_name)
                    print_length = line
            # remove excess text from line in file        
                    print_length = print_length.replace(r"<tr><td>Media</td><td>", "")
                    print_length = print_length.replace(r",", "")
                    print_length = re.sub (r"mm.*", "", print_length)
                    print_length2 = float(print_length)
                    print_length3 = int(print_length2)
                #print remaining text - print length in mm
            else:
                with open('printlength1.csv','a',newline='') as f:
                      writer=csv.writer(f)
                      writer.writerow([print_length3])
                with open('printlength.csv','a',newline='') as f:
                      writer=csv.writer(f)
                      writer.writerow([print_length3, (""), file_name])
    else:
            current_path = "".join((parent, "/", file_name))
scan_folder(".")  # Insert parent directory's path

print ("")
print ("Completed")
print ("")
total = 0
with open("printlength1.csv") as file:
   for row in csv.reader(file, delimiter=','):
        for col in row:
            total += int(col)
total2 = str(total)
print ("Total print length "+total2+" mm")
print ("")
try:
    os.remove("printlength1.csv")
except IOError:
    print ("")
input ("press enter to exit.")
