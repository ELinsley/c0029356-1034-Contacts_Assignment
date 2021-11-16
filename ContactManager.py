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
        """Fills a list of contacts instantiated from a text file"""
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

            ##self.contactList.append(Contact.Contact(name, address, phoneNumber, birthday))
            self.AddNewContact(name,address,phoneNumber,birthday)
            ##print(self.contactList[i].Get_Name()) ##Debug

    def GetContactDetails(self, index):
        """Returns all the details of the indexed contact"""
        details = self.contactList[index].Get_Details()
        details.insert(0,index)
        return  details

    def SearchContactName(self, name):
        """Searches for a contact by name, returns the list of contacts with that address."""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_Name() == name:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactAddress(self, address):
        """Searches for a contact by address, returns the list of contacts with that address."""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_Address() == address:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactPhoneNumber(self, phoneNumber):
        """Searches for a contact by phone number, returns the list of contacts with that address."""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_PhoneNumber() == phoneNumber:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactBirthday(self, birthday):
        """Searches for a contact by birthday, returns the list of contacts with that address."""
        exists = False
        resultList = []

        for i in range(len(self.contactList)):
            if self.contactList[i].Get_Birthday()[0:10] == birthday:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def EditContactName(self, index, name):
        """Edits the indexed contact, replacing the previous value for their name."""
        self.contactList[index].Set_Name(name)

    def EditContactAddress(self, index, address):
        """Edits the indexed contact, replacing the previous value for their address."""
        self.contactList[index].Set_Address(address)

    def EditContactPhoneNumber(self, index, phoneNumber):
        """Edits the indexed contact, replacing the previous value for their birthday."""
        self.contactList[index].Set_PhoneNumber(phoneNumber)

    def EditContactBirthday(self, index, birthday):
        """Edits the indexed contact, replacing the previous value for their birthday."""
        self.contactList[index].Set_Birthday(birthday)

    def AddNewContact(self, name, address, phoneNumber, birthday):
        """Adds a new contact with name, address, phoneNumber and birthday. Returns the new contact object."""
        self.contactList.append(Contact.Contact(name,address,phoneNumber,birthday))
        #print("Contact added...") ##Debug
        return self.contactList[len(self.contactList)-1]

    def DeleteContact(self, index):
        """Deletes the indexed contact from the contact list and returns the contact object that was deleted."""
        return self.contactList.pop(index)

    def SaveContacts(self):
        """Saves all the details in contactList to the text file, overwriting the previous content."""
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


    def __str__(self):
        return "I am the contact manager class, I have: " + len(self.contactList)