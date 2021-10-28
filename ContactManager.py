class ContactManager:

    contactList = []

    def __init__(self):
        """ContactManager class constructor"""
        self.LoadInContacts()

    def LoadInContacts(self):
        """Returns a list of contacts instantiated from a text file"""

        textFile = open("contactbook.txt", "r")
        fullText = textFile.read()
        textFile.close()

        print(fullText)
