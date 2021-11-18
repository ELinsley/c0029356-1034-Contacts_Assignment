import sysconfig
import sys

import ContactManager
import TestFile

import re # Used for regular expressions


def Display_Contacts_UI():
    """Loops through the list of contacts, printing all the details of each one"""
    for i in range(contact_Manager.Get_ContactList_Length()):
        contactDetails = contact_Manager.Get_Contact_Details(i)
        print("ID: " + str(contactDetails[0]) + ", Name: " + contactDetails[1] + ", Address: " + contactDetails[2] + ", Phone Number: " + contactDetails[3] + ", Birthday: " + contactDetails[4])
    input("Press enter to continue...")

def Search_Contacts_UI():
    """CLI that allows the user to select a detail to search against, and input the detail to look for"""
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
    valid_input = False
    while valid_input == False:  ## For sanitising files
        user_input = input("Enter your selection here: ")

        if user_input == "1":  ########## Name search
            valid_input = True
            search_input = input("What name would you like to search for?: ")

            results = contact_Manager.Search_Contact_Name(search_input)
            if len(results) == 0:
                print("There are no contacts with that name...")
            else:
                print("These are the contacts with that name:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif user_input == "2":  ########## Address search
            valid_input = True
            search_input = input("What address would you like to search for?: ")

            results = contact_Manager.Search_Contact_Address(search_input)
            if len(results) == 0:
                print("There are no contacts with that address...")
            else:
                print("These are the contacts with that address:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif user_input == "3":  ########## Phone number search
            valid_input = True
            print("Phone numbers are always 10 numerical characters, e.g. 7945625056")
            search_input = input("What phone number would you like to search for?: ")
            results = contact_Manager.Search_Contact_PhoneNumber(search_input)

            if len(results) == 0:
                print("There are no contacts with that phone number...")
            else:
                print("These contacts have that phone number:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif user_input == "4":  ########## Birthday Search
            valid_input = True
            print("Birthdays are always in the form of dd/mm/yyyy, e.g. 10/07/2002")
            search_input = input("What birthday would you like to search for?: ") ##Sanitise

            results = contact_Manager.Search_Contact_Birthday(search_input)
            if len(results) == 0:
                print("There are no contacts with that birthday...")
            else:
                print("These contacts have that birthday:")
                for i in range(len(results)):
                    print("ID: " + str(results[i][0]) + ", Name: " + results[i][1] + ", Address: " + results[i][2] + ", Phone Number: " + results[i][3] + ", Birthday: " + results[i][4])

        elif user_input == "Exit":
            valid_input = True
            print("Exit has been selected...")
        else:
            print("That is not a valid input, please try again...")
    input("Press enter to continue...")

def Edit_Contact_UI():
    """CLI that allows the user to select a contact to edit by ID, select which detail to edit, and input the detail"""
    print("")  ##Creates an empty line
    print("+--------Edit---------+")
    print("| Enter the ID of the |")
    print("| contact you would   |")
    print("| like to edit.       |")
    print("+---------------------+")

    valid_input = False
    while valid_input == False:
        edit_ID = input("Enter the ID here: ")

        if not (re.fullmatch("[0-9]+", edit_ID)):  ##Makes sure the input is made of only numericals
            print("The ID may only contain numbers, please try again...")
        else:
            edit_ID = int(edit_ID)
            if (edit_ID < contact_Manager.Get_ContactList_Length()) and (
                    edit_ID >= 0):  ##Makes sure input is within the range of possible contacts
                valid_input = True
            else:
                print("There is no contact with that ID, please try again...")
    print("")
    print(contact_Manager.Get_Contact_Details(edit_ID)[1] + " has been selected...")
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

    valid_input = False
    selected_detail = input("Enter your selection: ")
    while valid_input == False:  ## For sanitising inputs
        if selected_detail == "1":
            print("'Change name' selected...")
            valid_input = True
            print("")
            new_detail = input("Enter a new name here: ")
            contact_Manager.Edit_Contact_Name(edit_ID, new_detail)

        elif selected_detail == "2":
            print("'Change address' selected...")
            valid_input = True
            print("")
            new_detail = input("Enter new address here: ")
            contact_Manager.Edit_Contact_Address(edit_ID, new_detail)

        elif selected_detail == "3":
            print("'Change phone number' selected...")
            valid_input = True
            print("")
            new_detail = VerifyPhoneNumber(input("Enter new phone number here: "))
            contact_Manager.Edit_Contact_PhoneNumber(edit_ID, new_detail)

        elif selected_detail == "4":
            print("'Change birthday' selected...")
            valid_input = True
            print("")
            new_detail = input("Enter new birthday here: ")
            contact_Manager.Edit_Contact_Birthday(edit_ID, new_detail)

        elif selected_detail == "Exit":
            print("'Exit' selected...")
            valid_input = True
        else:
            print("That is not a valid input...")
    input("Press enter to continue...")

def Add_New_Contact_UI():
    """CLI that allows the user to input details for a new contact"""
    print()
    name = input("Enter the contacts full name here: ")
    address = input("Enter the contacts full address here: ")
    phoneNumber = VerifyPhoneNumber(input("Enter the contacts phone number here: "))
    birthday = input("Enter the contacts birthday here: ")

    contact_Manager.Add_New_Contact(name,address,phoneNumber,birthday)

    input("Press enter to continue...")

def Delete_Contact_UI():
    """CLI that allows the user to input an ID of the contact they want deleted"""
    print("")  ##Creates an empty line
    print("+-------Delete--------+")
    print("| Enter the ID of the |")
    print("| contact you would   |")
    print("| like to delete.     |")
    print("+---------------------+")

    valid_input = False
    while valid_input == False:
        edit_ID = input("Enter the ID here: ")

        if not (re.fullmatch("[0-9]+", edit_ID)):  ##Makes sure the input is made of only numericals
            print("The ID may only contain numbers, please try again...")
        else:
            edit_ID = int(edit_ID)
            if (edit_ID < contact_Manager.Get_ContactList_Length()) and (
                    edit_ID >= 0):  ##Makes sure input is within the range of possible contacts
                valid_input = True
            else:
                print("There is no contact with that ID, please try again...")

    deleted_contact = contact_Manager.Delete_Contact(edit_ID)

    print(deleted_contact.Get_Name() + " has been deleted...")
    input("Press enter to continue...")

def VerifyPhoneNumber(phoneNumber):
    """Loops until a phone number of valid format is input by the user, has no other break. Returns valid phone number."""
    valid_input = False
    while not valid_input:
        if re.fullmatch("[0-9]{10}", phoneNumber):
            valid_input = True
        else:
            print(phoneNumber)  ## Debug
            print("Phone numbers must consist of exactly 10 numerical characters, please try again.")
            phoneNumber = input("Enter phone number here: ")
    return phoneNumber

def VerifyBirthday(birthday):
    """Loops until birthday of valid format is input by the user, returns that value, has no other break condition."""
    valid_input = False
    while not valid_input:
        if re.fullmatch("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",birthday): # Checks to makes sure birthday is dd/mm/yyyy exactly
            valid_input=True;
        else:
            print("Birthdays must be of the form dd/mm/yyyy, eg 29/03/1995, please try again...")
            birthday = input("Enter birthday here: ")
    return birthday

if __name__ == "__main__" \
        and TestFile.TestAuto("Davidiom Testerino", "999 Testable Rd, Testsite 4, Manchester", "9999999999", "99/99/9999")\
        and TestFile.TestAuto("TESTTESTTESTTESTTESTTESTTESTTEST", "1010110101011010101010101100110", "0000990000", "00/99/0000"):
    # ^^ Runs an auto test with a variety of different contact details, main doesnt run if they fail (or dont fail) ^^ #

    contact_Manager = ContactManager.ContactManager() # Instantiating this immediately loads all contact details from the .txt

    user_input=""
    while user_input != "Exit":
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
        user_input = input("Enter your selection here: ")
        if user_input == "1":
            print("'Display all contacts' selected...")
            Display_Contacts_UI()
        elif user_input == "2":
            print("'Search for a contact' selected...")
            Search_Contacts_UI()
        elif user_input == "3":
            print("'Edit a contact' selected...")
            Edit_Contact_UI()
        elif user_input == "4":
            print("'Add a contact' selected...")
            Add_New_Contact_UI()
        elif user_input == "5":
            print("'Delete a contact' selected...")
            Delete_Contact_UI()
        elif user_input == "6":
            print("'Save changes' selected...")
            contact_Manager.Save_Contacts()
        elif user_input == "Exit":
            print("Saving and quitting...")
            contact_Manager.Save_Contacts()
        else:
            print("That is not a valid input, please try again...") ##Add exceptions