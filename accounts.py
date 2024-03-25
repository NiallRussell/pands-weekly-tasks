#This program reads in a 10 character account number and outputs the number with only the last four digits showing and the other digits replaced by an "X"
#Author: Niall Russell 


# Defining a function which checks if account number is 10 digits long. If so, it runs through each digit and replaces the digit with an "X" if the digit is in position 0-5. 
# If number inputted is not 10 digits long, it prints error message
def inputnumber():
    # Prompting the user to input their number
    fullnumber = input("Please enter a 10 digit account number: ")
    # Converting the string to a list to allow for cycling through items
    listnumber = list(fullnumber)
    # If length of list is 10 then replace the first 6 digits with "X", if not equal to 10 then print error message
    if len(listnumber) == 10:
        # For loop to cycle through items in the list- using enumerate method to keep track of each element and its position on the list: https://www.simplilearn.com/tutorials/python-tutorial/enumerate-in-python#:~:text=Python's%20enumerate%20method%20allows%20you,its%20position%20on%20a%20list.
        for i, v in enumerate(listnumber):
            # If item position is 5 or less (first position in the list is 0)
            if i <= 5:
                # Change the corresponding digit to "X"
                listnumber[i] = "X"
        # Convert the list back to a string for readability when printing- join function can join an iterable like a list. Using ''.join for no spaces between characters. 
        xnumber = ''.join(listnumber)
        # Print the encoded number
        print(xnumber)
    # If length of number is not equal to 10, print error message                    
    else:
        print("Number must be 10 digits long")

#Calling the function        
inputnumber()


