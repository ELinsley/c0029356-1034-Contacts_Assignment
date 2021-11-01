import Contact
import re

class ContactManager():

    contactList = []
    print("Contact Manager class exists") ##Debug

    def __init__(self):
        """ContactManager class constructor"""
        print("ContactManager has been constructed") ##Debug

        self.LoadInContacts()

    def LoadInContacts(self):
        """Returns a list of contacts instantiated from a text file"""
        ##print("LoadInContacts has been called") ##Debug

        textFile = open("contactbook.txt", "r")
        fullText = textFile.readlines()
        ##print(fullText)  ##Debug
        textFile.close()

        for i in range(len(fullText)-1):

            splitText = fullText[i].split("'")

            name = splitText[0]
            address = splitText[1]
            phoneNumber = splitText[2]
            birthday = splitText[3]

            self.contactList.append(Contact.Contact(name, address, phoneNumber, birthday))
            ##print(self.contactList[i].Get_Name()) ##Debug

    def MainMenu(self):
        """Brings up the main menu UI, then calls other functions based on user"""
        print("+-------------------------+")
        print("| 1) Display all contacts |")
        print("| 2) Search for a contact |")
        print("| 3) Edit a contact       |")
        print("| 4) Delete a contact     |")
        print("| 5) Save changes         |")
        print("| Enter 'Exit' to save    |")
        print("| and quit.               |")
        print("+-------------------------+")
        print("(1-4 / Exit)")

        validInput = False
        userInput = input("Enter your selection here: ")
        while validInput == False:
            if userInput == "1":
                print("'Display all contacts' selected...")
                validInput = True
                self.DisplayAllContacts()
            elif userInput == "2":
                print("'Search for a contact' selected...")
                validInput = True
                self.searchContacts()
            elif userInput == "3":
                print("'Edit a contact' selected...")
                validInput = True
                self.editContact()
            elif userInput == "4":
                print("'Delete a contact' selected...")
                validInput = True
            elif userInput == "Exit":
                print("'Exit' selected...")
                validInput=True
            else:
                print("That is not a valid input, please try again...")

        return userInput ##might not need

    def DisplayAllContacts(self):
        """Displays all the details of all existing contacts"""
        print("")
        for i in range(len(self.contactList)-1):
            details = self.contactList[i].Get_Details()
            print("ID: " + str(i) + ", Name: " + details[0] + ", Address: " + details[1] + ", Phone Number: " + details[2] + ", Birthday: " + details[3][0:10])

    def searchContacts(self):
        """Allows the user to search for a contact by name, address, phone number or birthday"""
        print("")
        print("+-------------------------+")
        print("| 1) Search Names         |")
        print("| 2) Search Address's     |")
        print("| 3) Search Phone Numbers |")
        print("| 4) Search Birthdays     |")
        print("| Enter 'Exit' to return  |")
        print("| to menu.                |")
        print("+-------------------------+")
        print("(1-4 / Exit)")
        validInput = False
        while validInput == False:
            userInput = input("Enter your selection here: ")

            if userInput == "1":
                validInput = True
                searchParam = input("What name would you like to search for?: ")
                exists = False
                for i in range(len(self.contactList)-1):
                    if self.contactList[i].Get_Name() == searchParam:
                        self.contactList[i].PrintDetails()
                        exists = True
                if exists == False:
                    print("No contacts were found with that name...")

            elif userInput =="2":
                validInput = True
                searchParam = input("What address would you like to search for?: ")
            elif userInput =="3":
                validInput = True
                print("Phone numbers are always 10 numerical characters, e.g. 7945625056")
                searchParam = input("What phone number would you like to search for?: ")
            elif userInput =="4":
                validInput = True
                print("Birthdays are always in the form of dd/mm/yyyy, e.g. 10/07/2002")
                searchParam = input("What birthday would you like to search for?: ")
            elif userInput == "Exit":
                validInput = True
                print("Exit has been selected...")
            else:
                print("That is not a valid input, please try again...")


    def editContact(self):
        """Brings up editContact UI and allows the user to edit a contact"""
        print("") ##Creates an empty line
        print("+---------------------+")
        print("| Enter the ID of the |")
        print("| contact you would   |")
        print("| like to edit.       |")
        print("+---------------------+")

        validInput = False
        while validInput == False:
            editID = input("Enter the ID here: ")

            if not (re.fullmatch("[0-9]+",editID)): ##Makes sure the input is made of only numericals
                print("The ID may only contain numbers, please try again...")
            else:
                editID = int(editID)
                if (editID < len(self.contactList)) and (
                        editID >= 0):  ##Makes sure input is within the range of possible contacts
                    validInput = True
                else:
                    print("There is no contact with that ID, please try again...")

        print("")
        print(self.contactList[editID].Get_Name() + " has been selected...")
        print("")
        print("+------------------------+")
        print("| 1) Change Name         |")
        print("| 2) Change Address      |")
        print("| 3) Change Phone Number |")
        print("| 4) Change Birthday     |")
        print("| Enter 'Exit' to return |")
        print("| to menu.               |")
        print("+------------------------+")
        print("(1-4 / Exit)")

        validInput = False
        editColumn = input("Enter your selection: ")
        while validInput == False:
            if editColumn == "1":
                print("'Change name' selected...")
                validInput = True
                print("")
                editDetail = input("Enter a new name here: ")
                self.contactList[editID].Set_Name(editDetail)

            elif editColumn == "2":
                print("'Change address' selected...")
                validInput = True
                print("")
                editDetail = input("Enter new address here: ")
                self.contactList[editID].Set_Address(editDetail)

            elif editColumn == "3":
                print("'Change phone number' selected...")
                validInput = True
                print("")
                editDetail = input("Enter new phone number here: ")
                self.contactList[editID].Set_PhoneNumber(editDetail)

            elif editColumn == "4":
                print("'Change birthday' selected...")
                validInput = True
                print("")
                editDetail = input("Enter new birthday here: ")
                self.contactList[editID].Set_Address(editDetail)

            elif editColumn == "Exit":
                print("'Exit' selected...")
                validInput = True
            else:
                print("That is not a valid input...")

        self.contactList[editID].PrintDetails() ##Debug