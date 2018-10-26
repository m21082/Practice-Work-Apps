# Find all instances of job name and show what material was ordered and on which date
# Info from CSV populated by material order script

import csv
import os
import sys
import time
from pathlib import Path
from time import gmtime, strftime

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
