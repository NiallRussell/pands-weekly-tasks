#Program which reads in a text file and outputs the number of 'E's it contains
#Author: Niall Russell

#Importing sys module to allow for command line arguments- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
import sys

#Start count at 0
total = 0

#Checking there is an argument in the command line. The programme name is the first argument, 
#so no argument is given when length is 1 or below- https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
if len(sys.argv) <= 1:
    print("No argument in command line")
#Checking if the file name ends with ".txt"- https://www.grepper.com/answers/242311/check+if+file+is+txt+python
elif not sys.argv[1].endswith(".txt"):
    print ("Not a text file")
#If argument exists and does not end with something other than '.txt', attempt to perform operation. 
#However, file can still not exist as have just proved that argument ends with ".txt"
else:
    #trying to open file and throwing an error message if does not exist
    #https://stackoverflow.com/questions/57007680/how-to-handle-the-exception-when-input-file-does-not-exists-in-python
    try: 
        #Open file in read mode- this will open first file entered into command line after the programme file 
        with open(sys.argv[1], "r") as f:
            #Read each line
            for line in f:
                #Store total "e" count for each line in variable "x"
                x = line.count("e")
                #Add x to the total
                total = total + x
        #print total
        print(total)
    # if file is not found, print error message
    except FileNotFoundError:
        print('File does not exist')

