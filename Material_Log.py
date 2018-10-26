# Store print info into xls files for Signs, Promo and Other jobs

import csv

print ()
print ("Print job material log")
print ()

while True:
    print ()

    
    # Prompt user for company division
    while True:
        division = input ("Company Division: (S)igns   (P)romo   (O)ther:  ")
        if division in["S", "s", "P", "p", "O", "o"]:
            if division == "S" or division == "s":
                division = "Signs"
            elif division == "P" or division == "p":
                division = "Promo"
            elif division == "O" or division == "o":
                division = "Other"
            break


    # Prompt user for end client    
    client = (input("Name of client or job reference:  "))


    # Prompt user for material
    while True:
        material = input ("Base Material: (W)hite   (C)lear   (P)VC   (R)oller   (O)ther:  ")
        if material in["W", "w", "C", "c", "P", "p", "R", "r", "O", "o"]:
            if material == "W" or material == "w":
                material = "White"
            elif material == "C" or material == "c":
                material = "Clear"
            elif material == "P" or material == "p":
                material = "PVC"
            elif material == "R" or material == "r":
                material = "Roller"
            elif material == "O" or material == "o":
                material = "Other"
            break


    # Prompt user for laminate
    while True:
        laminate = input ("Laminate Used: (M)att   (G)loss   (N)o Laminate   (O)ther:  ")
        if laminate in["M", "m", "G", "g", "N", "n", "O", "o"]:
            if laminate == "M" or laminate == "m":
                laminate = "Matt Laminate"
            elif laminate == "G" or laminate == "g":
                laminate = "Gloss Laminate"
            elif laminate == "N" or laminate == "n":
                laminate = "No Laminate"
            elif laminate == "O" or laminate == "o":
                laminate = "Other Laminate"
            break


    # Prompt user for job print length
    separator = " "
    length = sum(map(int, input("Length of print mm: ").split(separator)))
    length2 = str(length)


    # Display summary of inputs
    print ()
    print ("\n".join([division, "Client/Job ref: "+client, "Print onto "+material, "Laminate - "+laminate, "Print length "+length2+"mm"]))
    print ()


    # Ask user if info is correct
    while True:
        result = input ("Is the above info correct? Y/N: ")
        if result in["Y", "y", "N", "n"]:
            if result == "Y" or result == "y":
                result = "Yes"
            elif result == "N" or result == "n":
                result = "No"
            break


    # If correct then write to file, if incorrect then loop to start
    # If division = promo then save to promo csv
    # If division = signs then save to signs csv
    # If division = other then save to other csv
    while True:
        if result == "Yes" and division == "Signs":
            print ("Writing data to file")
            with open('signscsv.csv','a',newline='') as f:
                writer=csv.writer(f)
                writer.writerow([client, material, laminate, length2])
                print ("Completed")
                print ()
                # print("Press Enter to quit")
                # input()
        elif result == "Yes" and division == "Promo":
            print ("Writing data to file")
            with open('promocsv.csv','a',newline='') as f:
                writer=csv.writer(f)
                writer.writerow([client, material, laminate, length2])
                print ("Completed")
                print ()
                # print("Press Enter to quit")
                # input()
        elif result == "Yes" and division == "Other":
            print ("Writing data to file")
            with open('othercsv.csv','a',newline='') as f:
                writer=csv.writer(f)
                writer.writerow([client, material, laminate, length2])
                print ("Completed")
                print ()
                # print("Press Enter to quit")
                # input()
        elif result == "No":
            print ()
            # print("Press Enter to quit")
            # input()
        break


    # ask if user wants to input another record
    # loop back to start or exit program
    return_to_start = input ("Enter Y to add another record, any other input to quit")
    if return_to_start in ["Y", "y"]:
            # clear values for all inputs before restart
            division = ""
            client = ""
            material = ""
            laminate = ""
            length = ""
            continue
    else:
        break
