import Contact
import ContactManager
import main


def TestAuto(name, address, phoneNumber, birthday):
    """Automatically tests all the ContactManager functions, using the input name, address, phoneNumber, birthday"""
    testSuccess = True

    testName = name
    testAddress = address
    testPhoneNumber = phoneNumber
    testBirthday = birthday

################ Testing AddContact #################

    print("Adding test contact "+ testName +" : "+ testAddress +" : "+ testPhoneNumber + " : "+ testBirthday)
    testContactManager = ContactManager.ContactManager()
    testContactManager.AddNewContact(testName, testAddress, testPhoneNumber, testBirthday)
    testID = testContactManager.GetCListLength() - 1
    if testContactManager.GetContact(testID).Get_Name() == testName:
        print("Last contact added is "+ testContactManager.GetContact(testID).Get_Name())
        print("Test contact added succesfully...")
    else:
        print("! Last contact added is named "+testContactManager.GetContact(testID).Get_Name())
        print("! Test contact was not added succesfully!..")
        testSuccess = False

################ SearchContactName ###################

    print("Searching for the test contact "+testName+" by each detail...")
    testSearch = testContactManager.SearchContactName(testName)

    if len(testSearch) == 1:
        if testSearch[0][1] == testName:
            print("Succesfully found the test contact when searching by name, it is: " + testSearch[0][1] + "...")
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
            print("Succesfully found the test contact when searching by address, it is: " + testSearch[0][2] + "...")
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
            print("Succesfully found the test contact when searching by phoneNumber, it is: " + testSearch[0][3] + "...")
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
            print("Succesfully found the test contact when searching by birthday, it is: " + testSearch[0][4] + "...")
        else:
            print("! Searching by birthday returned a contact, but not the test contact!..")
            testSuccess = False
    else:
        print("! Wrong number of contacts found when searching by birthday, should only be 1!..")
        testSuccess = False

################ Testing EditContact #################

    editName = testName+"Test"
    testContactManager.EditContactName(testID, editName)
    if testContactManager.GetContact(testID).Get_Name() == editName:
        print("Test contact name has been correctly edited to ("+editName+"), it is now (" +testContactManager.GetContact(testID).Get_Name()+ ")...")
    else:
        print("! Test contact name has not been correctly edited!..")
        print(testContactManager.GetContact(testID).Get_Name())
        testSuccess = False

    editAddress = testAddress+"Test"
    testContactManager.EditContactAddress(testID, editAddress)
    if testContactManager.GetContact(testID).Get_Address() == editAddress:
        print("Test contact address has been correctly edited to ("+editAddress+"), it is now (" +testContactManager.GetContact(testID).Get_Address()+ ")...")
    else:
        print("! Test contact address has not been correctly edited!..")
        print(testContactManager.GetContact(testID).Get_Address())
        testSuccess = False

    editPhoneNumber = "0000000000"
    testContactManager.EditContactPhoneNumber(testID, editPhoneNumber)
    if testContactManager.GetContact(testID).Get_PhoneNumber() == editPhoneNumber:
        print("Test contact phone number has been correctly edited to ("+editPhoneNumber+"), it is now (" +testContactManager.GetContact(testID).Get_PhoneNumber()+ ")...")
    else:
        print("! Test contact phone number has not been correctly edited!..")
        print(testContactManager.GetContact(testID).Get_PhoneNumber())
        testSuccess = False

    editBirthday = "00/00/0000"
    testContactManager.EditContactBirthday(testID, editBirthday)
    if testContactManager.GetContact(testID).Get_Birthday() == editBirthday:
        print("Test contact birthday has been correctly edited to " + editBirthday + ", it is now (" +testContactManager.GetContact(testID).Get_Birthday()+ ")...")
    else:
        print("! Test contact birthday has not been correctly edited!..")
        print(testContactManager.GetContact(testID).Get_Birthday())
        testSuccess = False

    ############ Deleting a Contact ############

    testContactManager.DeleteContact(testContactManager.GetCListLength()-1)
    if testContactManager.GetContact(testContactManager.GetCListLength()-1).Get_Name() != editName: ##Is the last contact the same as the edited test one?
        print("Contact succesfully deleted, the contact at the end of the list is now " + testContactManager.GetContact(testContactManager.GetCListLength()-1).Get_Name())
    else:
        print("! Contact has not been deleted succesfully!..")
        testSuccess = False

    print("End of test.")
    print("")
    return testSuccess