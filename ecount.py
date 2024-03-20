#Write a program that reads in a text file and outputs the number of e's it contains. 
#Think about what is being asked here, document any assumptions you are making.
#The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
#Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

#Importing sys module to allow for command line arguments- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
import sys

#Start count at 0
total = 0

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
except FileNotFoundError:
    print('File does not exist')
