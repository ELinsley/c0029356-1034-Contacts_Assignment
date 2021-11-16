import ContactManager
import TestFile

import re #regular expressions


def DisplayContactsUI():
    print(contactManager.contactList)
    for i in range(len(contactManager.contactList)):
        contactDetails = contactManager.GetContactDetails(i)
        print("ID: " + str(contactDetails[0]) + ", Name: " + contactDetails[1] + ", Address: " + contactDetails[2] + ", Phone Number: " + contactDetails[3] + ", Birthday: " + contactDetails[4])
    input("Press enter to continue...")

def SearchContactsUI():
    print("")
    print("+---------Search----------+")
    print("| 1) Search Names         |")
    print("| 2) Search Address's     |")
    print("| 3) Search Phone Numbers |")
    print("| 4) Search Birthdays     |")
    print("| Enter 'Exit' to return  |")
    print("| to menu.                |")
    print("+-------------------------+")
    print("(1-4 / Exit)")
    validInput = False
    while validInput == False:  ## For sanitising files
        userInput = input("Enter your selection here: ")

        if userInput == "1":  ########## Name search
            validInput = True
            searchParam = input("What name would you like to search for?: ")

            results = contactManager.SearchContactName(searchParam)
            if len(results) == 0:
                print("There are no contacts with that name...")
            else:
                print("These are the contacts with that name:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif userInput == "2":  ########## Address search
            validInput = True
            searchParam = input("What address would you like to search for?: ")

            results = contactManager.SearchContactAddress(searchParam)
            if len(results) == 0:
                print("There are no contacts with that address...")
            else:
                print("These are the contacts with that address:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif userInput == "3":  ########## Phone number search
            validInput = True
            print("Phone numbers are always 10 numerical characters, e.g. 7945625056")
            searchParam = input("What phone number would you like to search for?: ")
            results = contactManager.SearchContactPhoneNumber(searchParam)

            if len(results) == 0:
                print("There are no contacts with that phone number...")
            else:
                print("These contacts have that phone number:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif userInput == "4":  ########## Birthday Search
            validInput = True
            print("Birthdays are always in the form of dd/mm/yyyy, e.g. 10/07/2002")
            searchParam = input("What birthday would you like to search for?: ") ##Sanitise

            results = contactManager.SearchContactBirthday(searchParam)
            if len(results) == 0:
                print("There are no contacts with that birthday...")
            else:
                print("These contacts have that birthday:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif userInput == "Exit":
            validInput = True
            print("Exit has been selected...")
        else:
            print("That is not a valid input, please try again...")
    input("Press enter to continue...")

def EditContactUI():
    print("")  ##Creates an empty line
    print("+--------Edit---------+")
    print("| Enter the ID of the |")
    print("| contact you would   |")
    print("| like to edit.       |")
    print("+---------------------+")

    validInput = False
    while validInput == False:
        editID = input("Enter the ID here: ")

        if not (re.fullmatch("[0-9]+", editID)):  ##Makes sure the input is made of only numericals
            print("The ID may only contain numbers, please try again...")
        else:
            editID = int(editID)
            if (editID < len(contactManager.contactList)) and (
                    editID >= 0):  ##Makes sure input is within the range of possible contacts
                validInput = True
            else:
                print("There is no contact with that ID, please try again...")
    print("")
    print(contactManager.GetContactDetails(editID)[1] + " has been selected...")
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
    while validInput == False:  ## For sanitising inputs
        if editColumn == "1":
            print("'Change name' selected...")
            validInput = True
            print("")
            editDetail = input("Enter a new name here: ")
            contactManager.EditContactName(editID, editDetail)

        elif editColumn == "2":
            print("'Change address' selected...")
            validInput = True
            print("")
            editDetail = input("Enter new address here: ")
            contactManager.EditContactAddress(editID, editDetail)

        elif editColumn == "3":
            print("'Change phone number' selected...")
            validInput = True
            print("")
            editDetail = VerifyPhoneNumber(input("Enter new phone number here: "))
            contactManager.EditContactPhoneNumber(editID, editDetail)

        elif editColumn == "4":
            print("'Change birthday' selected...")
            validInput = True
            print("")
            editDetail = input("Enter new birthday here: ")
            contactManager.EditContactBirthday(editID, editDetail)

        elif editColumn == "Exit":
            print("'Exit' selected...")
            validInput = True
        else:
            print("That is not a valid input...")
    input("Press enter to continue...")

def AddNewContactUI():
    print()
    name = input("Enter the contacts full name here: ")
    address = input("Enter the contacts full address here: ")
    phoneNumber = VerifyPhoneNumber(input("Enter the contacts phone number here: "))
    birthday = input("Enter the contacts birthday here: ")

    contactManager.AddNewContact(name,address,phoneNumber,birthday)

    input("Press enter to continue...")

def DeleteContactUI():
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
            if (editID < len(contactManager.contactList)) and (
                    editID >= 0):  ##Makes sure input is within the range of possible contacts
                validInput = True
            else:
                print("There is no contact with that ID, please try again...")

    deletedContact = contactManager.DeleteContact(editID)

    print(deletedContact.Get_Name() + " has been deleted...")
    input("Press enter to continue...")

def VerifyPhoneNumber(phoneNumber):
    """Loops until a phone number of valid format is input by the user, has no other break. Returns valid phone number."""
    validInput = False
    while not validInput:
        if re.fullmatch("[0-9]{10}", phoneNumber):
            validInput = True
        else:
            print(phoneNumber)  ## Debug
            print("Phone numbers must consist of exactly 10 numerical characters, please try again.")
            phoneNumber = input("Enter phone number here: ")
    return phoneNumber

def VerifyBirthday(birthday):
    """Loops until birthday of valid format is input by the user, returns that value, has no other break condition."""
    validInput = False
    while not validInput:
        if re.fullmatch("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",birthday): # Checks to makes sure birthday is dd/mm/yyyy exactly
            validInput=True;
        else:
            print("Birthdays must be of the form dd/mm/yyyy, eg 29/03/1995, please try again...")
            birthday = input("Enter birthday here: ")
    return birthday


if __name__ == "__main__" \
        and TestFile.TestAuto("Davidiom Testerino", "999 Testable Rd, Testsite 4, Manchester", "9999999999", "99/99/9999")\
        and TestFile.TestAuto("TESTTESTTESTTESTTESTTESTTESTTEST", "1010110101011010101010101100110", "0000990000", "00/99/0000"):
    contactManager = ContactManager.ContactManager() ## This also loads all contacts

    userInput=""
    while userInput != "Exit":
        print("")
        print("+---------Contacts---------+")
        print("| 1) Display all contacts. |")
        print("| 2) Search for a contact. |")
        print("| 3) Edit a contact.       |")
        print("| 4) Add a contact.        |")
        print("| 5) Delete a contact.     |")
        print("| 6) Save changes.         |")
        print("| Enter 'Exit' to save     |")
        print("| and quit.                |")
        print("+--------------------------+")
        print("(1-4 / Exit)")
        userInput = input("Enter your selection here: ")
        if userInput == "1":
            print("'Display all contacts' selected...")
            DisplayContactsUI()
        elif userInput == "2":
            print("'Search for a contact' selected...")
            SearchContactsUI()
        elif userInput == "3":
            print("'Edit a contact' selected...")
            EditContactUI()
        elif userInput == "4":
            print("'Add a contact' selected...")
            AddNewContactUI()
        elif userInput == "5":
            print("'Delete a contact' selected...")
            DeleteContactUI()
        elif userInput == "6":
            print("'Save changes' selected...")
            contactManager.SaveContacts()
        elif userInput == "Exit":
            print("Saving and quitting...")
            contactManager.SaveContacts()
        else:
            print("That is not a valid input, please try again...") ##Add exceptions