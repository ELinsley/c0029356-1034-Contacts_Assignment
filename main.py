import ContactManager
import TestFile

def DisplayContactsUI():
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

if __name__ == "__main__":
    ##print("Main") ## Debug
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
            contactManager.EditContact()
        elif userInput == "4":
            print("'Add a contact' selected...")
            contactManager.AddNewContact()
        elif userInput == "5":
            print("'Delete a contact' selected...")
            contactManager.DeleteContact()
        elif userInput == "6":
            print("'Save changes' selected...")
            contactManager.SaveContacts()
        elif userInput == "Exit":
            print("Saving and quitting...")
            contactManager.SaveContacts()
        else:
            print("That is not a valid input, please try again...")