import re

class Contact():

    ##print("Contact class exists") ##Debug

    def __init__(self, name, address, phoneNumber, birthday):
        """Contact class constructor"""
        ##print("Contact class constructor has been called") ##Debug
        self.Set_Name(name)
        self.Set_Address(address)
        self.Set_PhoneNumber(phoneNumber)
        self.Set_Birthday(birthday) #dd/mm/yyyy

    def PrintDetails(self):
        """Displays all contact details"""
        print(self.Get_Name(), " | ", self.Get_Address(), " | ", self.Get_PhoneNumber(), " | ", self.Get_Birthday())

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
        self.__name = name

    def Set_Address(self, address):
        self.__address = address

    def Set_PhoneNumber(self, phoneNumber):
        validInput = False
        while not validInput:
            if re.fullmatch("[0-9]{10}",phoneNumber):
                self.__phoneNumber = phoneNumber
                validInput = True
            else:
                phoneNumber = input("Phone numbers must consist of exactly 10 numerical characters, please try again: ")


    def Set_Birthday(self, birthday):
        self.__birthday = birthday