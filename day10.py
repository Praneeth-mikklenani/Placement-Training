#file handling --> manipulating files
#store data in files and use it later
#read data from files and write data to files
#update data in files and delete data from files
#.txt files or .csv files

#file modes
#r --> read a file
#w --> write to a file
#a --> append to a file
#x --> create a  new file
#r+ --> read and write to a file
#w+ --> write and read to a file
#a+ --> append and read to a file

#read --> methods
#read(),readline(), readlines()

#read() --> reads the entire file and returns it as a string
#readline() --> reads a single line from the file and returns it as a string
#readlines() --> reads all the lines of the file and returns it as a list of strings


file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec.txt", "r") #open a file in read mode
print(file.read()) #read the file and print it
file.close() #close the file

file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec.txt", "r") #open a file in read mode
print(file.readline()) #read the first line of the file and print it
print(file.readline()) #read the second line of the file and print it
file.close() #close the file

file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec.txt", "r") #open a file in read mode
print(file.readlines()) #read all the lines of the file and print it as a list
file.close() #close the file


#write --> methods
#write() --> writes a string to the file
#writelines() --> writes a list of strings to the file

file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec.txt", "w") #open a file in write mode
file.write("we are learning file handling") #write a string to the file and overwrite the existing content of the file
file.close() #close the file

file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec.txt", "r") #open the file in read mode
print(file.read()) #read the file and print it
file.close() #close the file
#prints --> we are learning file handling


#append --> adds new content to the end of the file without overwriting the existing content
file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec.txt", "a") #open a file in append mode
file.write("\n using append adding new line") #append a string to the file
file.close() #close the file

file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec.txt", "r") #open the file in read mode
print(file.read()) #read the file and print it
file.close() #close the file
#prints -->we are learning file handling using append adding new line


#create a new file using x mode
file = open(r"C:\Users\prajw\Desktop\Placement Training\Rymec1.txt", "x") #create a new file in x mode
file.close() #close the file

file = open("Rymec1.txt", "w") #open the file in write mode
file.write("this is a new file created using x mode") #write a string to the file
file.close() #close the file

file = open("Rymec1.txt", "r") #open the file in read mode
print(file.read()) #read the file and print it
file.close() #close the file

#difference between r+ and w+ mode
#r+ --> opens the file for both reading and writing. The file pointer is placed at the beginning of the file. If the file does not exist, it raises a FileNotFoundError.
#w+ --> opens the file for both writing and reading. The file pointer is placed at the beginning of the file. If the file does not exist, it creates a new file.


#file.seek() --> moves the file pointer to a specific position in the file
# i am learning python
#^  ^   ^        ^(read pointer)
#move the read pointer to the beginning 
#file.seek(0) 

file= open("Rymec1.txt", "w+") #open the file in write and read mode
file.write("i am learning python") #write a string to the file
file.seek(0) #move the read pointer to the beginning of the file
print(file.read()) #read the file and print it
file.close() #close the file
