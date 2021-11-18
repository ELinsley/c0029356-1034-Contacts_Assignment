import re

class Contact():
    """Contact class that stores name, address, phonenumber and birthday. Getters and Setters exist for all details."""

    def __init__(self, name, address, phoneNumber, birthday):
        """Contact class constructor. Takes name, address, phonenumber, birthday"""
        self.Set_Name(name)
        self.Set_Address(address)
        self.Set_PhoneNumber(phoneNumber)
        self.Set_Birthday(birthday) #dd/mm/yyyy

    def Get_Details(self):
        """Returns all contact details"""
        return [self.Get_Name(), self.Get_Address(), self.Get_PhoneNumber(), self.Get_Birthday()]

############### Getters ################

    def Get_Name(self):
        return self.__name

    def Get_Address(self):
        return self.__address

    def Get_PhoneNumber(self):
        return self.__phoneNumber

    def Get_Birthday(self):
        return self.__birthday


############### Setters ################

    def Set_Name(self, name):
        self.__name = self.remove_apostrophes(str(name))

    def Set_Address(self, address):
        self.__address = self.remove_apostrophes(str(address))

    def Set_PhoneNumber(self, phoneNumber):
        self.__phoneNumber = self.remove_apostrophes(str(phoneNumber))

    def Set_Birthday(self, birthday): ## Input needs to be sanitised
        self.__birthday = self.remove_apostrophes(birthday)



    def remove_apostrophes(self, string):
        """returns the input string but with all apostrophes removed"""
        for i in range(len(string)):
            if string[i] == "'":
                string.pop(i)
        return string

    def __str__(self):
        """Returns class details in one string"""
        return("I am a contact class, here are my details: " + self.Get_Name(), " | ", self.Get_Address(), " | ", self.Get_PhoneNumber(), " | ", self.Get_Birthday())
