import ContactManager
import TestFile

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
            contactManager.DisplayAllContacts()
        elif userInput == "2":
            print("'Search for a contact' selected...")
            contactManager.SearchContacts()
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