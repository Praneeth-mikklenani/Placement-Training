# #access the characters in a string by using the index number inside square brackets
# #indexing starts at 0, so the first character is at index 0, the second character is at index 1, and so on
# #positive indexing starts from the left, while negative indexing starts from the right and negative index -1 refers to the last character, -2 refers to the second last character, and so on
# #p y t h o n
# #0 1 2 3 4 5
str="python"
print(str[0]) #p
print(str[1]) #y
print(str[2]) #t
print(str[3]) #h
print(str[4]) #o
print(str[5]) #n

# #negative indexing
# # p  y  t  h  o  n
# #-6 -5 -4 -3 -2 -1
str="python"
print(str[-1]) #n
print(str[-2]) #o
print(str[-3]) #h
print(str[-4]) #t
print(str[-5]) #y
print(str[-6]) #p

# #string slicing
# #slicing allows you to extract a portion of a string by specifying the start and end index
# #string slicing syntax: string[start:end:step]
str="python programming"
print(str[0:6]) #python
print(str[7:18]) #programming
print(str[:6]) #python
print(str[7:]) #programming
print(str[0:6:2]) #pto
print(str[7:18:3]) #pormg


# #strings are immutable, which means that you cannot change the characters in a string after it has been created. However, you can create a new string by concatenating or slicing existing strings.
str1="hello"
str1[0]='H' #this will raise an error because strings are immutable

str="PYTHON"
#convert the string to lowercase
print(str.lower()) #python
#convert the string to uppercase
print(str.upper()) #PYTHON
#capitalize the first character of the string
print(str.capitalize()) #Python

# #checking string properties

# #isdigit() method checks if all characters in the string are digits (0-9) and there is at least one character. It returns True if the string is a digit, and False otherwise.
s="123"
print(s.isdigit()) #True

# #isalpha() method checks if all characters in the string are alphabetic (letters) and there is at least one character. It returns True if the string is alphabetic, and False otherwise.
s="abc"
print(s.isalpha()) #True

# #isalnum() method checks if all characters in the string are alphanumeric (letters and numbers) and there is at least one character. It returns True if the string is alphanumeric, and False otherwise.
s="abc123"
print(s.isalnum()) #True

# #search in string
# #find() method returns the index of the first occurrence of the specified substring in the string. If the substring is not found, it returns -1.
str="python programming"
print(str.find("program")) #7

# #search method returns the index of the first occurrence of the specified substring in the string. If the substring is not found, it returns -1.
s="python programming"
print(s.find("t",2)) #2

# str="Google"
print(str.count("o")) #2

# #replace() method replaces all occurrences of a specified substring with another substring in the string. It returns a new string with the replacements made.
str="python programming"
new_str=str.replace("python","java")
print(new_str) #java programming


# # #split() method splits a string into a list of substrings based on a specified delimiter. By default, the delimiter is whitespace (space, tab, newline).
s="a,b,c"
print(s.split(",")) #['a', 'b', 'c']

# #delimiter is the character or string that separates the substrings in the original string. The split() method returns a list of substrings that were separated by the delimiter.

# #join() method is used to join a list of strings into a single string using a specified delimiter. The syntax is: delimiter.join(list_of_strings)
list_of_strings=["a","b","c"]
delimiter=","
result=delimiter.join(list_of_strings)
print(result) #a,b,c

#Check whether the given string is a palindrome or not.
str=input("Enter a string: ")
if str==str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#Check whether two strings are anagrams or not.
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
if sorted(str1)==sorted(str2):
    print("The strings are anagrams.") 
else:
    print("The strings are not anagrams.") 
