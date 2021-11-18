import Contact
import re

class ContactManager():

    def __init__(self):
        """ContactManager class constructor, !calls Load_In_Contacts!"""
        self.__contactList = []
        self.Load_In_Contacts()

    def Load_In_Contacts(self):
        """Fills a list with Contact class instantiated from contacts.txt"""
        text_file = open("contactbook.txt", "r")
        full_text = text_file.readlines() # reads in ALL the text into a list, split by newline
        text_file.close()

        for i in range(len(full_text)):
            split_text = full_text[i].split("'") # Creates a list, seperating the full_text on apostrophes
            name = split_text[0]
            address = split_text[1]
            phoneNumber = split_text[2]
            birthday = split_text[3][0:10]

            self.Add_New_Contact(name,address,phoneNumber,birthday)

    def Get_Contact_Details(self, index):
        """Returns all the details of the indexed contact as a list. Adding the index of the contact in the list to the front."""
        details = self.__contactList[index].Get_Details()
        details.insert(0,index) # Adds the index of the contact to the front of the list of details
        return  details

    def Get_Contact(self, index):
        return self.__contactList[index]

    def Search_Contact_Name(self, name):
        """Checks every contact for a name that matches the input, returns a list that contains lists of details"""
        exists = False
        result_list = []

        for i in range(self.Get_ContactList_Length()):
            if self.__contactList[i].Get_Name() == name:
                result_list.append(self.Get_Contact_Details(i))
        return result_list

    def Search_Contact_Address(self, address):
        """Checks every contact for a address that matches the input, returns a list that contains lists of details."""
        exists = False
        result_list = []

        for i in range(self.Get_ContactList_Length()):
            if self.__contactList[i].Get_Address() == address:
                result_list.append(self.Get_Contact_Details(i))
        return result_list

    def Search_Contact_PhoneNumber(self, phoneNumber):
        """Checks every contact for a phone number that matches the input, returns a list that contains lists of details"""
        exists = False
        result_list = []

        for i in range(self.Get_ContactList_Length()):
            if self.__contactList[i].Get_PhoneNumber() == phoneNumber:
                result_list.append(self.Get_Contact_Details(i))
        return result_list

    def Search_Contact_Birthday(self, birthday):
        """Checks every contact for a birthday that matches the input, returns a list that contains lists of details"""
        exists = False
        result_list = []

        for i in range(self.Get_ContactList_Length()):
            if self.__contactList[i].Get_Birthday()[0:10] == birthday:
                result_list.append(self.Get_Contact_Details(i))
        return result_list

    def Edit_Contact_Name(self, index, name):
        """Edits the indexed contact, replacing the previous value for their name with the arg."""
        self.__contactList[index].Set_Name(name)

    def Edit_Contact_Address(self, index, address):
        """Edits the indexed contact, replacing the previous value for their address with the arg."""
        self.__contactList[index].Set_Address(address)

    def Edit_Contact_PhoneNumber(self, index, phoneNumber):
        """Edits the indexed contact, replacing the previous value for their phone number with the arg."""
        self.__contactList[index].Set_PhoneNumber(phoneNumber)

    def Edit_Contact_Birthday(self, index, birthday):
        """Edits the indexed contact, replacing the previous value for their birthday with the arg."""
        self.__contactList[index].Set_Birthday(birthday)

    def Add_New_Contact(self, name, address, phoneNumber, birthday):
        """Adds a new contact with name, address, phoneNumber and birthday. Returns the new contact object."""
        self.__contactList.append(Contact.Contact(name,address,phoneNumber,birthday))
        return self.__contactList[self.Get_ContactList_Length()-1]

    def Delete_Contact(self, index):
        """Deletes the indexed contact from the contact list and returns the contact object that was deleted."""
        return self.__contactList.pop(index)

    def Save_Contacts(self):
        """Saves all the details in __contactList to the text file, overwriting the previous content."""
        text_file = open("contactbook.txt","w")
        for i in range(self.Get_ContactList_Length()):
            if i == self.Get_ContactList_Length(): # (If this is the last entry in the list, dont include a \n at the end)
                text_file.write(self.__contactList[i].Get_Name() + "'" +
                                self.__contactList[i].Get_Address() + "'" +
                                self.__contactList[i].Get_PhoneNumber() + "'" +
                                self.__contactList[i].Get_Birthday()
                               )
            else:
                text_file.write(self.__contactList[i].Get_Name() + "'" +
                                self.__contactList[i].Get_Address() + "'" +
                                self.__contactList[i].Get_PhoneNumber() + "'" +
                                self.__contactList[i].Get_Birthday() + "\n"
                                )
        text_file.close()

    def Get_ContactList_Length(self):
        """Returns the length of the __contactList"""
        return len(self.__contactList)

    def __str__(self):
        """Returns some detail about the class"""
        return "I am the contact manager class, I have: " + self.self.Get_ContactList_Length() + " contacts that I manage."