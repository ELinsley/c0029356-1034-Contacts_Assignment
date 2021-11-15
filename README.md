How to Use
==========

###Overview of the application





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

###How to use

On running, a text ui is printed to the #### menu. Enter the number of the option
you would like to use when prompted. When prompted, enter details as specified.

After completing a task, the user must press enter to continue back to the main menu.

Any changes made will not be immediately saved, you must either enter Exit at
the main menu, or 5 to save without quitting.

###Use Case

####Editing a contact:
At the main menu, enter 1 on the prompt line. This will then display all contacts and
their IDs. Press enter to return to main menu, then enter 3 to edit contacts. Enter
the ID of the contact the user want to edit, e.g 3. Enter 1 to edit the name of the
contact. Then enter the new name at the prompt, e.g Johnathon Jameson. Press enter
to continue.