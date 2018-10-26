# Script found online and modified
# Practice script


from random import randint

secret_number = randint(1, 11)
#print (secret_number)

while True:
    try:
        user_number = int(input("Enter a number (1-10): "))
        if user_number in range(0,100):
            if user_number == secret_number:
                print ()
                print ()
                print ("######################")
                print ("#                    #")
                print ("#  Correct Number!!  #")
                print ("#                    #")
                print ("######################")                
                print ()
                print ()
                break
            else:
                print ()
                print ("#   #          #   #")
                print (" # #            # # ")
                print ("  #    WRONG     #  ")
                print (" # #            # # ")
                print ("#   #          #   #")                
                print ()
                continue
    except ValueError:
        print("Please enter a number (1-10)")
    else:
        continue
