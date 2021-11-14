How to Use
==========

On running, a text ui is printed to the #### menu. Enter the number of the option
you would like to use when prompted.
From the main menu, entering 1 will display all details of all saved contacts.

Any changed made will not be immediately saved, you must either enter Exit at
the main menu, or 5 to save without quitting.

-------------------------------------------

###Assumptions

Assumes nationality of phone numbers isnt needed, so all phone numbers are exactly 10
characters long (so no 0 or +44, etc.)

Assumes no ones name, address, phone number or birthday contains an apostrophe, as
this character is used as the delimeter in the text file that stores the details.
e.g Joe'London'0192837465'01/02/3456

Assumes users understand what is meant by dd/mm/yyyy as this is the only accepted
format for birthday input.

Assumes user won't lie about their details, as the program only validates the formats,
it doesn't check if the inputs are actually true/valid.

Assumes no one has the following details: David Tester : 35 Auto Tst, Teston, Testfordshire : 1234567890 : 01/02/3000
as these are all used for the test contact.