import Contact
import ContactManager

def Test_Auto(name, address, phoneNumber, birthday):
    """Automatically tests all the ContactManager functions, using the input name, address, phoneNumber, birthday"""
    test_success = True

    test_name = name
    test_address = address
    test_phonenumber = phoneNumber
    test_birthday = birthday

################ Testing AddContact #################

    print("Adding test contact "+ test_name +" : "+ test_address +" : "+ test_phonenumber + " : "+ test_birthday)
    test_contact_manager = ContactManager.ContactManager()
    test_contact_manager.Add_New_Contact(test_name, test_address, test_phonenumber, test_birthday)
    test_ID = test_contact_manager.Get_ContactList_Length() - 1
    if test_contact_manager.Get_Contact(test_ID).Get_Name() == test_name:
        print("Last contact added is "+ test_contact_manager.Get_Contact(test_ID).Get_Name())
        print("Test contact added successfully...")
    else:
        print("! Last contact added is named "+test_contact_manager.Get_Contact(test_ID).Get_Name())
        print("! Test contact was not added successfully!..")
        test_success = False

################ Search_Contact_Name ###################

    print("Searching for the test contact "+test_name+" by each detail...")
    test_search = test_contact_manager.Search_Contact_Name(test_name)

    if len(test_search) == 1:
        if test_search[0][1] == test_name:
            print("successfully found the test contact when searching by name, it is: " + test_search[0][1] + "...")
        else:
            print("! Searching by name returned a contact, but not the test contact!..")
            test_success = False
    else:
        print("! Wrong number of contacts found when searching by name, should only be 1!..")
        test_success = False

############### Search_Contact_Address ##################

    test_search = test_contact_manager.Search_Contact_Address(test_address)

    if len(test_search) == 1:
        if test_search[0][2] == test_address:
            print("successfully found the test contact when searching by address, it is: " + test_search[0][2] + "...")
        else:
            print("! Searching by address returned a contact, but not the test contact!..")
            test_success = False
    else:
        print("! Wrong number of contacts found when searching by address, should only be 1!..")
        test_success = False

############### Search_Contact_PhoneNumber ##################

    test_search = test_contact_manager.Search_Contact_PhoneNumber(test_phonenumber)

    if len(test_search) == 1:
        if test_search[0][3] == test_phonenumber:
            print("successfully found the test contact when searching by phoneNumber, it is: " + test_search[0][3] + "...")
        else:
            print("! Searching by phone number returned a contact, but not the test contact!..")
            test_success = False
    else:
        print("! Wrong number of contacts found when searching by phone number, should only be 1!..")
        test_success = False

############### Search_Contact_Birthday ##################

    test_search = test_contact_manager.Search_Contact_Birthday(test_birthday)

    if len(test_search) == 1:
        if test_search[0][4] == test_birthday:
            print("successfully found the test contact when searching by birthday, it is: " + test_search[0][4] + "...")
        else:
            print("! Searching by birthday returned a contact, but not the test contact!..")
            test_success = False
    else:
        print("! Wrong number of contacts found when searching by birthday, should only be 1!..")
        test_success = False

################ Testing EditContact #################

    edit_name = test_name+"Test"
    test_contact_manager.Edit_Contact_Name(test_ID, edit_name)
    if test_contact_manager.Get_Contact(test_ID).Get_Name() == edit_name:
        print("Test contact name has been correctly edited to ("+edit_name+"), it is now (" +test_contact_manager.Get_Contact(test_ID).Get_Name()+ ")...")
    else:
        print("! Test contact name has not been correctly edited!..")
        print(test_contact_manager.Get_Contact(test_ID).Get_Name())
        test_success = False

    edit_address = test_address+"Test"
    test_contact_manager.Edit_Contact_Address(test_ID, edit_address)
    if test_contact_manager.Get_Contact(test_ID).Get_Address() == edit_address:
        print("Test contact address has been correctly edited to ("+edit_address+"), it is now (" +test_contact_manager.Get_Contact(test_ID).Get_Address()+ ")...")
    else:
        print("! Test contact address has not been correctly edited!..")
        print(test_contact_manager.Get_Contact(test_ID).Get_Address())
        test_success = False

    edit_phonenumber = "0102030405"
    test_contact_manager.Edit_Contact_PhoneNumber(test_ID, edit_phonenumber)
    if test_contact_manager.Get_Contact(test_ID).Get_PhoneNumber() == edit_phonenumber:
        print("Test contact phone number has been correctly edited to ("+edit_phonenumber+"), it is now (" +test_contact_manager.Get_Contact(test_ID).Get_PhoneNumber()+ ")...")
    else:
        print("! Test contact phone number has not been correctly edited!..")
        print(test_contact_manager.Get_Contact(test_ID).Get_PhoneNumber())
        test_success = False

    edit_birthday = "01/02/0304"
    test_contact_manager.Edit_Contact_Birthday(test_ID, edit_birthday)
    if test_contact_manager.Get_Contact(test_ID).Get_Birthday() == edit_birthday:
        print("Test contact birthday has been correctly edited to " + edit_birthday + ", it is now (" +test_contact_manager.Get_Contact(test_ID).Get_Birthday()+ ")...")
    else:
        print("! Test contact birthday has not been correctly edited!..")
        print(test_contact_manager.Get_Contact(test_ID).Get_Birthday())
        test_success = False

    ############ Deleting a Contact ############

    test_contact_manager.Delete_Contact(test_contact_manager.Get_ContactList_Length()-1)
    if test_contact_manager.Get_Contact(test_contact_manager.Get_ContactList_Length()-1).Get_Name() != edit_name: ##Is the last contact the same as the edited test one?
        print("Contact successfully deleted, the contact at the end of the list is now " + test_contact_manager.Get_Contact(test_contact_manager.Get_ContactList_Length()-1).Get_Name())
    else:
        print("! Contact has not been deleted successfully!..")
        test_success = False

    print("End of test.")
    print("")
    return test_success


if __name__ == "__main__":
    test_success = True

    try:
        print("This test should pass...")
        if not Test_Auto("David Tester", "4 Test Rd, Teston", "0192837465", "01/23/1986"): # Normal
            test_success = False
    except:
        print("An error was encountered during the normal test...")
        test_success = False

    try:
        print("This test should pass...")
        if not Test_Auto("MY NAME IS NUMBERS ¬¬¬¬ 9999999999999999999", "999999999999999999999999999999999999rfrv99gr99999999999999999", "9999999999", "99/99/9999"): # Upper bound
            test_success = False
    except:
        print("An error was encountered during the upper test...")
        test_success = False

    try:
        print("This test should pass...")
        if not Test_Auto("", "", "0000000000", "00/00/0000"): # Lower bound
            test_success = False
    except:
        print("An error was encountered during the lower test...")
        test_success = False

    try:
        print("This test should fail...")
        if Test_Auto("'-1'", "-'2", "phone", "secret"): # Outer bound
            test_success = False
    except:
        print("An error was encountered during the outer test...")
        #test_success = False

    if test_success:
        print("Tests all went as expected...")
    else:
        print("A test has failed at some point...")