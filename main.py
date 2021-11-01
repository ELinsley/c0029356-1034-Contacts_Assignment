import ContactManager

if __name__ == "__main__":
    ##print("Main") ## Debug
    contactManager = ContactManager.ContactManager() ##This also loads all contacts

    """Brings up the main menu UI, then calls other functions based on user"""
    print("+-------------------------+")
    print("| 1) Display all contacts |")
    print("| 2) Search for a contact |")
    print("| 3) Edit a contact       |")
    print("| 4) Delete a contact     |")
    print("| 5) Save changes         |")
    print("| Enter 'Exit' to save    |")
    print("| and quit.               |")
    print("+-------------------------+")
    print("(1-4 / Exit)")

    validInput = False
    userInput = input("Enter your selection here: ")
    while validInput == False:
        if userInput == "1":
            print("'Display all contacts' selected...")
            validInput = True
            contactManager.DisplayAllContacts()
        elif userInput == "2":
            print("'Search for a contact' selected...")
            validInput = True
            contactManager.searchContacts()
        elif userInput == "3":
            print("'Edit a contact' selected...")
            validInput = True
            contactManager.editContact()
        elif userInput == "4":
            print("'Delete a contact' selected...")
            validInput = True
        elif userInput == "Exit":
            print("'Exit' selected...")
            validInput=True
        else:
            print("That is not a valid input, please try again...")