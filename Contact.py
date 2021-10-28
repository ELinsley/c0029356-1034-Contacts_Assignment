
class Contact:

    __name = ""
    __address = ""
    __phoneNumber = ""
    __birthday = ""

    def __init__(self, name, address, phoneNumber, birthday):
        """Contact class constructor"""
        __name = name
        __address = address
        __phoneNumber = phoneNumber
        __birthday = birthday #dd/mm/yyyy

    def ShowDetails(self):
        """Displays all contact details"""
        print(self.Get_Name())
        print(self.Get_Address())
        print(self.Get_PhoneNumber())
        print(self.Get_Birthday())


############### Getters ################

    def Get_Name(self):
        print("Name goes here")
        return self.__name

    def Get_Address(self):
        print("Address goes here")
        return self.__address

    def Get_PhoneNumber(self):
        print("Phone number here")
        return self.__phoneNumber

    def Get_Birthday(self):
        print("Birthday goes here")
        return self.__birthday


############### Setters ################

    def Set_Name(self, name):
        self.__name = name

    def Set_Address(self, address):
        self.__address = address

    def Set_PhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def Set_Birthday(self, birthday):
        self.__birthday = birthday