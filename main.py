import ContactManager

if __name__ == "__main__":
    ##print("Main") ## Debug
    contactManager = ContactManager.ContactManager()

def MainMenu():
    print("+-------------------------+")
    print("| 1) Display all contacts |")
    print("| 2) Search for a contact |")
    print("| 3) Edit a contact       |")
    print("| 4) Delete a contact     |")
    print("| Enter 'Exit' to close   |")
    print("+-------------------------+")
    print("(1-4 / Exit)")
    userInput = input("Enter your selection: ")

    if userInput == "1":
        print("'Display all contacts' selected...")
    elif userInput == "2":
        print("'Search for a contact' selected...")
    elif userInput == "3":
        print("'Edit a contact' selected...")
        editContact()
    elif userInput == "4":
        print("'Delete a contact' selected...")
    elif userInput == "Exit":
        print("'Exit' selected...")
    return userInput

def editContact():
    print("+---------------------+")
    print("| Enter the ID of the |")
    print("| contact you would   |")
    print("| like to edit.       |")
    print("+---------------------+")
    editID = input("Enter the ID: ")

    print("+-----------------------+")
    print("| 1) Edit Name          |")
    print("| 2) Edit Address       |")
    print("| 3) Edit Phone Number  |")
    print("| 4) Edit Birthday      |")
    print("| Enter 'Exit' to close |")
    print("+-----------------------+")
    print("(1-4 / Exit)")
    editColumn = input("Enter your selection: ")

    contactManager.contactList[editID]