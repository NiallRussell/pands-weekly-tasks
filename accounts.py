#Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

#$ python accounts.py
#Please enter an 10 digit account number: 1234567890
#XXXXXX7890

def inputnumber():
    fullnumber = input("Please enter a 10 digit account number: ")
    listnumber = list(fullnumber)
    if len(listnumber) == 10:
        for i, v in enumerate(listnumber):
            if i <= 5:
                listnumber[i] = "X"
        xnumber = ''.join(listnumber)
        print(xnumber)                
    else:
        print("Number must be 10 digits long")
        
inputnumber()


