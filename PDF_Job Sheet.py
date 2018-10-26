# Fill in job sheet with user inputs
# Uses external pdf

import os
import sys
import fdfgen

# List of fields in external PDF
field_names = ["Job No", "Client", "Date", "Order No", "Client Address", "Site Address", "Details", "Description", "Previous Jobs"] 
all_fields = []

#Prompt the user to provide values for the above fields
for i in range(len(field_names)):
     field_value = input(field_names[i] + ": ") 
     all_fields.append((field_names[i], field_value))

#Create FDF file with these fields
fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
fdf_file = open("file_fdf.fdf","w") 
fdf_file.write(fdf_data.decode(fdf_file.encoding)) 
fdf_file.close()

#Run pdftk system command to populate the pdf file. The file "file_fdf.fdf" is pushed in to "input_pdf.pdf" thats generated as a new "output_pdf.pdf" file.
pdftk_cmd = "pdftk \input_pdf.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"
os.system(pdftk_cmd)

# Open pdf
os.system("start output_pdf.pdf")

#Remove the fdf file
os.remove("file_fdf.fdf")
