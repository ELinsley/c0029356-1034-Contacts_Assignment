import Contact

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
        validInput=False
        print("+-------------------------+")
        print("| 1) Display all contacts |")
        print("| 2) Search for a contact |")
        print("| 3) Edit a contact       |")
        print("| 4) Delete a contact     |")
        print("| Enter 'Exit' to save    |")
        print("| and quit.               |")
        print("+-------------------------+")
        print("(1-4 / Exit)")

        userInput = input("Enter your selection: ")
        while validInput == False:
            if userInput == "1":
                print("'Display all contacts' selected...")
                validInput = True
                self.DisplayAllContacts()
            elif userInput == "2":
                print("'Search for a contact' selected...")
                validInput = True
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
                print("That is not a valid input...")

        return userInput

    def DisplayAllContacts(self):
        print("")
        for i in range(len(self.contactList)-1):
            details = self.contactList[i].Get_Details()
            print("ID: " + str(i) + ", Name: " + details[0] + ", Address: " + details[1] + ", Phone Number: " + details[2] + ", Birthday: " + details[3][0:10])

    def editContact(self):
        """Brings up editContact UI and allows the user to edit a contact"""
        validInput = False
        print("") ##Creates an empty line
        print("+---------------------+")
        print("| Enter the ID of the |")
        print("| contact you would   |")
        print("| like to edit.       |")
        print("+---------------------+")

        while validInput == False: ###!!! Need to check if input is actually an integer at all !!!###
            editID = int(input("Enter the ID here: "))
            if (editID > len(self.contactList)-1) or (editID < 0):
                print("There is no contact with that ID...")
            else:
                validInput = True

        validInput = False
        print("")
        print(self.contactList[editID].Get_Name() + " has been selected...")
        print("")
        print("+--------------------------+")
        print("| 1) Change Name           |")
        print("| 2) Change Address        |")
        print("| 3) Change Phone Number   |")
        print("| 4) Change Birthday       |")
        print("| Enter 'Exit' to return   |")
        print("| to menu.                 |")
        print("+--------------------------+")
        print("(1-4 / Exit)")

        editColumn = input("Enter your selection: ")

        while validInput == False:
            if editColumn == "1":
                print("'Change name' selected...")
                validInput = True
                print("")
                editDetail = input("Enter a the new name here: ")
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