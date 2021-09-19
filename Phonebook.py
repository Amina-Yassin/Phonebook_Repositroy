import Directory_Module

c1 = Directory_Module.Contact_1
x1 = Directory_Module.Contact_1x
c2 = Directory_Module.Contact_2
x2 = Directory_Module.Contact_2x
c3 = Directory_Module.Contact_3
x3 = Directory_Module.Contact_3x
c4 = Directory_Module.Contact_4
x4 = Directory_Module.Contact_4x
c5 = Directory_Module.Contact_5
x5 = Directory_Module.Contact_5x

name = input("Hello user, welcome to the online phonebook. Please enter your name to begin. " )
print ("Greetings,", name, """. Here is the current list of available contacts. 
Please note that this is the beta version of this website, and there will be a limited number of contacts.""")

print ()
print ("1+",x1)
print ()
print ("2+",x2)
print ()
print ("3+",x3)
print ()
print ("4+",x4)
print ()
print ("5+",x5)
print ()

choice = input("To select a contact, please type in the letter x and the number corresponding to your selection. " )

if choice == "x1":
    print()
    print (c1)
elif choice == "x2":
    print ()
    print(c2)
elif choice == "x3":
    print ()
    print(c3)
elif choice == "x4":
    print ()
    print(c4)
elif choice == "x5":
    print ()
    print(c5)

(End_Continue) = input("Would you like to see another contact? 1 for yes, 2 for no. " )

if (End_Continue) == "1":
    choice = input("To select a contact, please type in the letter x and the number corresponding to your selection. " )
    if choice == "x1":
        print()
        print (c1)
    elif choice == "x2":
        print ()
        print(c2)
    elif choice == "x3":
        print ()
        print(c3)
    elif choice == "x4":
        print ()
        print(c4)
    elif choice == "x5":
        print ()
        print(c5)
    
    print ("Have a good day, and thank you for participating in the beta test of the Online Phonebook.")
    print ()

elif (End_Continue) == "2":
    print ("Have a good day, and thank you for participating in the beta test of the Online Phonebook.")
    print ()
    print ()
