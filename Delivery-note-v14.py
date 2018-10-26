# Delivery note script
# Fills in addresses from external csv
# Date, order numbers and items in delivery
# Fills in external pdf

import csv
import fdfgen
import os
import sys
import time

# remove any existing files from force quit etc.
try:
    os.remove("delivery_items.csv")
except IOError:
    print ("")

# get system date for filling in form
from time import gmtime, strftime
date = strftime("%d/%m/%Y", gmtime())

# get user input for form filling
def new_item_line():
    item_description = str(input ("Item description: "))
    item_cost = str(input ("Item price: £"))
    item_quantity = str(input ("Quantity: "))
    with open('delivery_items.csv','a',newline='') as f:
                writer=csv.writer(f)
                writer.writerow([item_description, item_cost, item_quantity])

# use external csv to populate common addresses
def address():
    with open("DeliveryAddressBook.csv", "r") as dab:
        dabreader = csv.reader(dab)
        rows = list(dabreader)
        full_address = rows[(+int(client))]
        all_fields.append(("line1", full_address[0]))
        all_fields.append(("line2", full_address[1]))
        all_fields.append(("line3", full_address[2]))
        all_fields.append(("line4", full_address[3]))
        all_fields.append(("line5", full_address[4]))
        all_fields.append(("line6", full_address[5]))
        all_fields.append(("line7", full_address[6]))

# main script
print ()
print ("Delivery note writer")

while True:
    print ()

    while True:
        print ()
        client = int(input ("Delivery Address:\n"
                        "1- Babcock\n"
                        "2- TCR\n"
                        "3- John Guest\n"
                        "4- Komfort\n"
                        "5- Cooley\n"
                        "6- Halfords Media\n"
                        "7- Hhopco\n"
                        "8- More options\n"
                        ": "))
        if client == 8:
                print ()
                client = int(input ("Delivery Address:\n"
                                "1- KLM\n"
                                "2- LTLGS\n"
                                "3- Sega\n"
                                "4- TSL\n"
                                "5- WJ Silvertown\n"
                                "6- Blank Address\n"
                                "7- Previous options\n"
                                ": "))
                if client == 1:
                    client = 8
                elif client == 2:
                    client = 9
                elif client == 3:
                    client = 10
                elif client == 4:
                    client = 11
                elif client == 5:
                    client = 12
                elif client == 6:
                    client = 13
                else:
                    continue
                break

        elif client == 1:
            client = 1
        elif client == 2:
            client = 2
        elif client == 3:
            client = 3
        elif client == 4:
            client = 4
        elif client == 5:
            client = 5
        elif client == 6:
            client = 6
        elif client == 7:
            client = 7
        else:
            continue
        break

    break

job_number = input("Aztec job number: ")

order_number = input ("Customer order number: ")

print()

# add more items to delivery note
while True:
    new_item_line()
    print()
    return_to_start = input ("Enter Y to add another item, any other input to finish: ")
    if return_to_start in ["Y", "y"]:
        # clear values for all inputs before restart
        item_description = ""
        item_cost = ""
        item_quantity = ""
        continue
    else:
        break

print ()

# write to pdf
with open("delivery_items.csv" ,"r") as csvfile:
    reader = csv.reader(csvfile,delimiter = ",")
    data = list(reader)
    n = 0
    field_names = [("pdftk input_pdf.pdf dump_data_fields")] 
    all_fields = []
    fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
    fdf_file = open("file_fdf.fdf" , "w" , encoding="ISO-8859-1")
    for row in data:
        n = n+1
        all_fields.append(("item"+str(n), row[0]))
        if row[1] == "":
            all_fields.append(("cost"+str(n), "See invoice"))
        else:
            all_fields.append(("cost"+str(n), "£"+row[1]))
        all_fields.append(("quant"+str(n), row[2]))
        fdf_file.write(fdf_data.decode(fdf_file.encoding)) 
    fdf_file.close()

    all_fields.append(("job_number", job_number))
    all_fields.append(("order_number", order_number))
    all_fields.append(("date", date))

    fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
    fdf_file = open("file_fdf.fdf" , "w" , encoding="ISO-8859-1") 
    fdf_file.write(fdf_data.decode(fdf_file.encoding)) 
    fdf_file.close()

    address()

    fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
    fdf_file = open("file_fdf.fdf" , "w" , encoding="ISO-8859-1") 
    fdf_file.write(fdf_data.decode(fdf_file.encoding)) 
    fdf_file.close()

    pdftk_cmd = "pdftk \input_pdf.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"
    os.system(pdftk_cmd)

    os.system("start output_pdf.pdf")

    os.remove("file_fdf.fdf")

# remove temp csv file
try:
    os.remove("delivery_items.csv")
except IOError:
    print ("")
