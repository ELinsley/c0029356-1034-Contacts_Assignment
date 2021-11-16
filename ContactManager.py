import Contact
import re

class ContactManager():

    ##__contactList = []
    ##print("Contact Manager class exists") ##Debug

    def __init__(self):
        """ContactManager class constructor, !calls LoadInContacts!"""
        self.__contactList = []
        self.LoadInContacts()

    def LoadInContacts(self):
        """Fills a list with Contact class instantiated from contacts.txt"""
        textFile = open("contactbook.txt", "r")
        fullText = textFile.readlines() # reads in ALL the text into a list, split by newline
        textFile.close()

        for i in range(len(fullText)):
            splitText = fullText[i].split("'") # Creates a list, seperating the fullText on apostrophes
            name = splitText[0]
            address = splitText[1]
            phoneNumber = splitText[2]
            birthday = splitText[3][0:10]

            self.AddNewContact(name,address,phoneNumber,birthday)

    def GetContactDetails(self, index):
        """Returns all the details of the indexed contact as a list. Adding the index of the contact in the list to the front."""
        details = self.__contactList[index].Get_Details()
        details.insert(0,index) # Adds the index of the contact to the front of the list of details
        return  details

    def GetContact(self, index):
        return self.__contactList[index]

    def SearchContactName(self, name):
        """Checks every contact for a name that matches the input, returns a list that contains lists of details"""
        exists = False
        resultList = []

        for i in range(self.GetCListLength()):
            if self.__contactList[i].Get_Name() == name:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactAddress(self, address):
        """Checks every contact for a address that matches the input, returns a list that contains lists of details."""
        exists = False
        resultList = []

        for i in range(self.GetCListLength()):
            if self.__contactList[i].Get_Address() == address:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactPhoneNumber(self, phoneNumber):
        """Checks every contact for a phone number that matches the input, returns a list that contains lists of details"""
        exists = False
        resultList = []

        for i in range(self.GetCListLength()):
            if self.__contactList[i].Get_PhoneNumber() == phoneNumber:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def SearchContactBirthday(self, birthday):
        """Checks every contact for a birthday that matches the input, returns a list that contains lists of details"""
        exists = False
        resultList = []

        for i in range(self.GetCListLength()):
            if self.__contactList[i].Get_Birthday()[0:10] == birthday:
                resultList.append(self.GetContactDetails(i))
        return resultList

    def EditContactName(self, index, name):
        """Edits the indexed contact, replacing the previous value for their name with the arg."""
        self.__contactList[index].Set_Name(name)

    def EditContactAddress(self, index, address):
        """Edits the indexed contact, replacing the previous value for their address with the arg."""
        self.__contactList[index].Set_Address(address)

    def EditContactPhoneNumber(self, index, phoneNumber):
        """Edits the indexed contact, replacing the previous value for their phone number with the arg."""
        self.__contactList[index].Set_PhoneNumber(phoneNumber)

    def EditContactBirthday(self, index, birthday):
        """Edits the indexed contact, replacing the previous value for their birthday with the arg."""
        self.__contactList[index].Set_Birthday(birthday)

    def AddNewContact(self, name, address, phoneNumber, birthday):
        """Adds a new contact with name, address, phoneNumber and birthday. Returns the new contact object."""
        self.__contactList.append(Contact.Contact(name,address,phoneNumber,birthday))
        return self.__contactList[self.GetCListLength()-1]

    def DeleteContact(self, index):
        """Deletes the indexed contact from the contact list and returns the contact object that was deleted."""
        return self.__contactList.pop(index)

    def SaveContacts(self):
        """Saves all the details in __contactList to the text file, overwriting the previous content."""
        textFile = open("contactbook.txt","w")
        for i in range(self.GetCListLength()):
            if i == self.GetCListLength(): # (If this is the last entry in the list, dont include a \n at the end)
                textFile.write(self.__contactList[i].Get_Name() + "'" +
                                self.__contactList[i].Get_Address() + "'" +
                                self.__contactList[i].Get_PhoneNumber() + "'" +
                                self.__contactList[i].Get_Birthday()
                               )
            else:
                textFile.write(self.__contactList[i].Get_Name() + "'" +
                                self.__contactList[i].Get_Address() + "'" +
                                self.__contactList[i].Get_PhoneNumber() + "'" +
                                self.__contactList[i].Get_Birthday() + "\n"
                                )
        textFile.close()

    def GetCListLength(self):
        """Returns the length of the __contactList"""
        return len(self.__contactList)

    def __str__(self):
        """Returns some detail about the class"""
        return "I am the contact manager class, I have: " + self.self.GetCListLength() + " contacts that I manage."