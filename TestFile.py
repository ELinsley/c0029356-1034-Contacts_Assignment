import Contact
import ContactManager
import main


def TestAuto(name, address, phoneNumber, birthday):

    testSuccess = True

    testName = name
    testAddress = address
    testPhoneNumber = phoneNumber
    testBirthday = birthday

################ Testing AddContact #################

    print("Adding test contact "+ testName +" : "+ testAddress +" : "+ testPhoneNumber + " : "+ testBirthday)
    testContactManager = ContactManager.ContactManager()
    testContactManager.AddNewContact(testName, testAddress, testPhoneNumber, testBirthday)
    testID = len(testContactManager.contactList) - 1
    if testContactManager.contactList[testID].Get_Name() == testName:
        print("Test contact added succesfully...")
    else:
        print("! Test contact was not added succesfully!..")
        testSuccess = False

################ SearchContactName ###################

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

############### SearchContactAddress ##################

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

############### SearchContactPhoneNumber ##################

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

############### SearchContactBirthday ##################

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

################ Testing EditContact #################

    testContactManager.EditContactName(testID, "")
    if testContactManager.contactList[testID].Get_Name() == "":
        print("Test contact name has been correctly edited...")
    else:
        print("! Test contact name has not been correctly edited!..")
        print(testContactManager.contactList[testID].Get_Name())
        testSuccess = False

    testContactManager.EditContactAddress(testID, "")
    if testContactManager.contactList[testID].Get_Address() == "":
        print("Test contact address has been correctly edited...")
    else:
        print("! Test contact address has not been correctly edited!..")
        print(testContactManager.contactList[testID].Get_Address())
        testSuccess = False

    testContactManager.EditContactPhoneNumber(testID, "0000000000")
    if testContactManager.contactList[testID].Get_PhoneNumber() == "0000000000":
        print("Test contact phone number has been correctly edited...")
    else:
        print("! Test contact phone number has not been correctly edited!..")
        print(testContactManager.contactList[testID].Get_PhoneNumber())
        testSuccess = False

    testContactManager.EditContactBirthday(testID, "00/00/0000")
    if testContactManager.contactList[testID].Get_Birthday() == "00/00/0000":
        print("Test contact birthday has been correctly edited...")
    else:
        print("! Test contact birthday has not been correctly edited!..")
        print(testContactManager.contactList[testID].Get_Birthday())
        testSuccess = False







    return testSuccess