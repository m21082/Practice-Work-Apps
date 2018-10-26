# Fills in pdf job sheet from access database
# Only user input is job number

import pypyodbc
import csv
import os
import re
import sys
import fdfgen

try:
    os.remove("jobs.csv")
except IOError:
    print ("")
try:
    os.remove("jobs1.csv")
except IOError:
    print ("")

Job_Number = input ("Job Number: ")

cnxn = pypyodbc.win_connect_mdb(r"\\aztec-dc\Companydrive\Database\aztec group.mdb")
cursor = cnxn.cursor()
cursor.execute ("SELECT * FROM Orders")


for row in cursor.fetchall():
    if Job_Number in row:
        print(row)

        with open('jobs1.csv','a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow([row])
        #with open('jobs.csv','a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow([row])

        #jobno = row[0]
        #client = row[5]

        # Input into pdf file
        field_names = ["Job No", "Client", "Date", "Order No", "Client Address", "Site Address", "Details", "Description", "Previous Jobs"] 
        all_fields = []

        all_fields.append(("Job No", row[0]))
        all_fields.append(("Client", row[3]))
        all_fields.append(("Date", row[2]))
        all_fields.append(("Order No", row[6]))
        all_fields.append(("Client Address", row[5]))
        all_fields.append(("Site Address", row[4]))
        all_fields.append(("Details", row[7]))


        #Create FDF file with these fields
        fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
        fdf_file = open("file_fdf.fdf" , "w" , encoding="ISO-8859-1") 
        fdf_file.write(fdf_data.decode(fdf_file.encoding)) 
        fdf_file.close()

        #Run pdftk system command to populate the pdf file. The file "file_fdf.fdf" is pushed in to "input_pdf.pdf" thats generated as a new "output_pdf.pdf" file.
        pdftk_cmd = "pdftk \input_pdf.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"
        os.system(pdftk_cmd)

        os.system("start output_pdf.pdf")

        #Remove the fdf file
        os.remove("file_fdf.fdf")

        #print (jobno)

cnxn.close()

try:
    os.remove("jobs.csv")
except IOError:
    print ("")
try:
    os.remove("jobs1.csv")
except IOError:
    print ("")
