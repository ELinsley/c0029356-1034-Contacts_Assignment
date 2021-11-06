import Contact
import re

class ContactManager():

    contactList = []
    ##print("Contact Manager class exists") ##Debug

    def __init__(self):
        """ContactManager class constructor"""
        ##print("ContactManager has been constructed") ##Debug

        self.LoadInContacts()

    def LoadInContacts(self):
        """Returns a list of contacts instantiated from a text file"""
        ##print("LoadInContacts has been called") ##Debug

        textFile = open("contactbook.txt", "r")
        fullText = textFile.readlines()
        ##print(fullText)  ##Debug
        textFile.close()

        for i in range(len(fullText)):

            splitText = fullText[i].split("'")

            name = splitText[0]
            address = splitText[1]
            phoneNumber = splitText[2]
            birthday = splitText[3][0:10]

            self.contactList.append(Contact.Contact(name, address, phoneNumber, birthday))
            ##print(self.contactList[i].Get_Name()) ##Debug

    def GetContactDetails(self, index):
        """Returns all the details of the indexed contact"""
        details = self.contactList[index].Get_Details()
        details.insert(0,index)
        return  details

    def SearchContactName(self, name):
        """Searches for a contact by name"""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_Name() == name:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactAddress(self, address):
        """Searches for a contact by address"""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_Address() == address:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactPhoneNumber(self, phoneNumber):
        """Searches for a contact by phone number"""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_PhoneNumber() == phoneNumber:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactBirthday(self, birthday):
        """Searches for a contact by birthday"""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_Birthday()[0:10] == birthday:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def EditContact(self):
        """Brings up editContact UI and allows the user to edit a contact"""
        print("") ##Creates an empty line
        print("+--------Edit---------+")
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
        print("+----------Edit----------+")
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
        while validInput == False: ## For sanitising inputs
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
                self.contactList[editID].Set_Birthday(editDetail)

            elif editColumn == "Exit":
                print("'Exit' selected...")
                validInput = True
            else:
                print("That is not a valid input...")
        self.contactList[editID].PrintDetails() ##Debug
        input("Press enter to continue...")

    def AddNewContact(self):
        """Allows the user to input the details of a new contact, which is then added as a contact"""
        print()
        name = input("Enter the contacts full name here: ")
        address = input("Enter the contacts full address here: ")

        validInput = False
        while not validInput:
            phoneNumber = input("Enter the contacts phone number here: ")
            if re.fullmatch("[0-9]{10}", phoneNumber): ##Checks if input is exactly 10 numerical characters
                self.__phoneNumber = phoneNumber
                validInput = True
            else:
                print(phoneNumber)  ## Debug
                print("Phone numbers must consist of exactly 10 numerical characters, please try again...")

        birthday = input("Enter the contacts birthday here: ")

        self.contactList.append(Contact.Contact(name, address, phoneNumber, birthday))
        self.contactList[len(self.contactList)-1].PrintDetails() ##Debug
        print("Contact added...")
        input("Press enter to continue...")

    def DeleteContact(self):
        """Delete a contact"""
        print("")  ##Creates an empty line
        print("+-------Delete--------+")
        print("| Enter the ID of the |")
        print("| contact you would   |")
        print("| like to delete.     |")
        print("+---------------------+")

        validInput = False
        while validInput == False:
            editID = input("Enter the ID here: ")

            if not (re.fullmatch("[0-9]+", editID)):  ##Makes sure the input is made of only numericals
                print("The ID may only contain numbers, please try again...")
            else:
                editID = int(editID)
                if (editID < len(self.contactList)) and (editID >= 0):  ##Makes sure input is within the range of possible contacts
                    validInput = True
                else:
                    print("There is no contact with that ID, please try again...")

        deletedContact = self.contactList.pop(editID)
        print(deletedContact.Get_Name() + " has been deleted...")
        input("Press enter to continue...")

    def SaveContacts(self):
        textFile = open("contactbook.txt","w")
        for i in range(len(self.contactList)):
            if i == len(self.contactList):
                textFile.write(self.contactList[i].Get_Name() + "'" +
                                self.contactList[i].Get_Address() + "'" +
                                self.contactList[i].Get_PhoneNumber() + "'" +
                                self.contactList[i].Get_Birthday()
                               )
            else:
                textFile.write(self.contactList[i].Get_Name() + "'" +
                                self.contactList[i].Get_Address() + "'" +
                                self.contactList[i].Get_PhoneNumber() + "'" +
                                self.contactList[i].Get_Birthday() + "\n"
                                )
        textFile.close()