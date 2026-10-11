# # This is a simple Python program that concatenates two strings and prints the result.
a="Hello"
b="World"
c=a+" "+b
print(c)

n=100
print((n%10)*10+(n//10))

# #relational operators
a=10
b=20
print(a==b) #False
print(a!=b) #True
print(a>b) #False
print(a<b) #True
print(a>=b) #False
print(a<=b) #True

a="apple"
b="orange"
print(a==b) #False
print(a!=b) #True
print(a>b) #False
print(a<b) #True
print(a>=b) #False
print(a<=b) #True

# #ascii values 
# #A=65, B=66, C=67, D=68, E=69, F=70, G=71, H=72, I=73, J=74, K=75, L=76, M=77, N=78, O=79, P=80, Q=81, R=82, S=83, T=84, U=85, V=86, W=87, X=88, Y=89, Z=90
# #a=97, b=98, c=99, d=100, e=101, f=102, g=103, h=104, i=105, j=106, k=107, l=108, m=109, n=110, o=111, p=112, q=113, r=114, s=115, t=116, u=117, v=118, w=119, x=120, y=121, z=122
# #0=48, 1=49, 2=50, 3=51, 4=52, 5=53, 6=54, 7=55, 8=56, 9=57

a="abc"
b="Abc"
print(a>b) #True
print(a<b) #True
print(a>=b) #False
print(a<=b) #True

# # The ord() function returns the Unicode code point for a given character.
print(ord('A')) #65
print(ord('a')) #97

# #The chr() function returns the character that corresponds to a given Unicode code point.
print("a" > "A")  #True  
print("abc" == "abc ") #False  
print("10" > "2") #False because in string comparison, "1" is less than "2" when compared character by character.


#logical operators
#and, or, not
#and: returns True if both operands are true, otherwise returns False
#or: returns True if at least one operand is true, otherwise returns False
#not: returns True if the operand is false, otherwise returns False

#and--> True and True = True
# True and False = False
# False and True = False
# False and False = False

#or--> True or True = True
# True or False = True
# False or True = True
# False or False = False

#not--> not True = False
# not False = True

print(10 and 20) #20 because in Python, the 'and' operator returns the first operand if it is falsy (e.g., 0, None, False), otherwise it returns the second operand. Since 10 is truthy, it returns 20.  
print(0 and 20) #0 because 0 is falsy, so the 'and' operator returns the first operand, which is 0.      
print(5 and 0) #0 because 0 is falsy, so the 'and' operator returns the first operand, which is 0.

print(False and print("Hello")) #False because the 'and' operator evaluates the first operand (False) and since it is falsy, it does not evaluate the second operand (print("Hello")) and returns False.
print(5 > 2 and 10 > 3 or 1 > 5) #True because the expression is evaluated as follows: (5 > 2) and (10 > 3) or (1 > 5) => True and True or False => True or False => True


# #control structures
# #1. conditional statements (make decisions based on conditions)
# #2. loops (repeat a block of code multiple times)
# #3. Jump statements (break or skip iterations in loops)

# #conditional statements -> used to execute a block of code based on a condition (true or false)
# #Types of conditional statements:
# #1. if statement
# #2. if-else statement
# #3. if-elif-else statement
# #4. nested if statement


# #if statement -> used to execute a block of code if a condition is true
age=int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")


# #if-else statement -> used to execute a block of code if a condition is true, and another block of code if the condition is false
# #given a number, check if it is even or odd
num=int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# #if-elif-else statement -> used to execute a block of code if a condition is true, and another block of code if the condition is false, and another block of code if the condition is false
#greatest of three numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)


# # #print the number is positive, negative or zero
num=int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# #nested if statement -> used to execute a block of code if a condition is true, and another block of code if the condition is false, and another block of code if the condition is false
# #check if a number is positive, negative or zero, and also check if it is even or odd
num=int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif num < 0:
    print("The number is negative.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


# #check wheather a given character is a vowel or consonant
char=input("Enter a character: ")
if char in 'aeiouAEIOU':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")


# #identify the type of a given character
char=input("Enter a character: ")
if char.isalpha():
    print("The character is an alphabet.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")


# #electrcity bill calculation
units = int(input("Enter the number of units consumed: "))
bill = 0
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    if bill > 500:
        bill = bill + bill * 0.10
print("The electricity bill is:", bill)


# #employee bonus calculation
salary = float(input("Enter salary: "))
if salary > 50000:
    bonus = salary * 0.10
elif salary > 30000:
    bonus = salary * 0.05
else:
    bonus = salary * 0.02
print("Bonus:", bonus)


#jumping statements -> used to break or skip iterations in loops
#types of jumping statements: 
#1. break statement -> used to exit a loop prematurely when a certain condition is met
#2. continue statement -> used to skip the current iteration of a loop and move to the next iteration
#3. pass statement -> used as a placeholder for future code, it does nothing when executed

#break statement example
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

#continue statement example
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip the current iteration if i is even
    print(i)

#pass statement example
for i in range(1, 11):
    if i==3:
        pass  # Placeholder for future code when i is 3
    print(i)

#print numbers from 1 to 20 skip multiples of 3 stop the loop completely when the number is divisible by 11
for i in range(1, 21):
    if i % 3 == 0:
        continue  # Skip multiples of 3
    if i % 11 == 0:
        break  # Stop the loop when the number is divisible by 11
    print(i, end="")
