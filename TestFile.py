import Contact
import ContactManager
import main

def TestAuto(name, address, phoneNumber, birthday):

    testSuccess = True

    testName = name
    testAddress = address
    testPhoneNumber = phoneNumber
    testBirthday = birthday

################ Testing ADD #################

    print("Adding test contact "+ testName +" : "+ testAddress +" : "+ testPhoneNumber + " : "+ testBirthday)
    testContactManager = ContactManager.ContactManager()
    testContactManager.AddNewContact(testName, testAddress, testPhoneNumber, testBirthday)
    if testContactManager.contactList[len(testContactManager.contactList)-1].Get_Name() == testName:
        print("Test contact added succesfully...")
    else:
        print("! Test contact was not added succesfully!..")
        testSuccess = False

################ Testing Search by Name ###################

    print("Searching for the test contact "+testName+" by each detail...")
    testSearch = testContactManager.SearchContactName(testName)

    if len(testSearch) == 1:
        if testSearch[0][1] == testName:
            print("Succesfully found the test contact when searching by name...")
        else:
            print("! Searching by name returned a contact, but not the test contact!..")
            testSuccess = False
    else:
        print("! Wrong number of contacts found when searching by name, should only be 1!..")
        testSuccess = False

############### Testing Search by Address ##################

    testSearch = testContactManager.SearchContactAddress(testAddress)

    if len(testSearch) == 1:
        if testSearch[0][2] == testAddress:
            print("Succesfully found the test contact when searching by address...")
        else:
            print("! Searching by address returned a contact, but not the test contact!..")
            testSuccess = False
    else:
        print("! Wrong number of contacts found when searching by address, should only be 1!..")
        testSuccess = False

############### Testing Search by phone number ##################

    testSearch = testContactManager.SearchContactPhoneNumber(testPhoneNumber)

    if len(testSearch) == 1:
        if testSearch[0][3] == testPhoneNumber:
            print("Succesfully found the test contact when searching by phone number...")
        else:
            print("! Searching by phone number returned a contact, but not the test contact!..")
            testSuccess = False
    else:
        print("! Wrong number of contacts found when searching by phone number, should only be 1!..")
        testSuccess = False

############### Testing Search by birthday ##################

    testSearch = testContactManager.SearchContactBirthday(testBirthday)

    if len(testSearch) == 1:
        if testSearch[0][4] == testBirthday:
            print("Succesfully found the test contact when searching by birthday...")
        else:
            print("! Searching by birthday returned a contact, but not the test contact!..")
            testSuccess = False
    else:
        print("! Wrong number of contacts found when searching by birthday, should only be 1!..")
        testSuccess = False





    return testSuccess