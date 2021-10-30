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
        print("| Enter 'Exit' to close   |")
        print("+-------------------------+")
        print("(1-4 / Exit)")

        userInput = input("Enter your selection: ")
        while validInput == False:
            if userInput == "1":
                print("'Display all contacts' selected...")
                validInput = True
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
            editID = input("Enter the ID here: ")
            if (editID > len(self.contactList)-1) or (editID < 0):
                print("There is no contact with that ID...")
            else:
                validInput = True

        validInput = False
        print("")
        print(self.contactList[editID].Get_Name() + " has been selected...")
        print("")
        print("+------------------------+")
        print("| 1) Edit Name           |")
        print("| 2) Edit Address        |")
        print("| 3) Edit Phone Number   |")
        print("| 4) Edit Birthday       |")
        print("| Enter 'Exit' to return |")
        print("| to menu.               |")
        print("+------------------------+")
        print("(1-4 / Exit)")

        editColumn = input("Enter your selection: ")

        while validInput == False:
            if editColumn == "1":
                print("'Edit name' selected...")
                validInput = True
                print("")
                editDetail = input("Enter new name here: ")
            elif editColumn == "2":
                print("'Edit address' selected...")
                validInput = True
                print("")
                editDetail = input("Enter new address here: ")
            elif editColumn == "3":
                print("'Edit phone number' selected...")
                validInput = True
                self.editContact()
                print("")
                editDetail = input("Enter new phone number here: ")
            elif editColumn == "4":
                print("'Edit birthday' selected...")
                validInput = True
                print("")
                editDetail = input("Enter new birthday here 'dd/mm/yyyy': ")
            elif editColumn == "Exit":
                print("'Exit' selected...")
                validInput = True
            else:
                print("That is not a valid input...")
