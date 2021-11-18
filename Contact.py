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
        self.__name = str(name)

    def Set_Address(self, address):
        self.__address = address

    def Set_PhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def Set_Birthday(self, birthday): ## Input needs to be sanitised
        validInput = False
        while not validInput:
            if re.fullmatch("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", birthday):
                self.__birthday = birthday
                validInput = True
            else:
                print(birthday)  ## Debug
                print("Birthdays must be of the form dd/mm/yyyy")
                birthday = input("Enter birthday here: ")


    def __str__(self):
        """Returns class details in one string"""
        return("I am a contact class, here are my details: " + self.Get_Name(), " | ", self.Get_Address(), " | ", self.Get_PhoneNumber(), " | ", self.Get_Birthday())
