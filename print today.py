# Search csv files for lines including todays date
# CSV files populated by material order script

import csv
import os
import sys
import time
from pathlib import Path
from time import gmtime, strftime

date = strftime("%d/%m/%Y", gmtime())

for file_name in os.listdir():
    if file_name.endswith(".csv"):
        print ()
        with open ((file_name), 'r') as f:
            csv_reader = csv.reader(f, delimiter=",")
            for row in csv_reader:
                if date in row:
                    print ("".join(row))

