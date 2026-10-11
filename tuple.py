#tuple -> Collection of elements, similar to list 
#maintains the insertion order
#allows duplicate elements
#immutable -> cannot be changed once created
#heterogeneous -> can contain different types of elements

#creating a tuple
#with parentheses
tuple=(1, 2, 3)
print(tuple)

#without parentheses
tuple=1, 2, 3
print(tuple)

#only one element
tuple=(1,)
print(tuple)

#accessing elements
tuple=(1, 2, 3, 4, 5)
print(tuple[0]) #1 #indexing starts from 0
print(tuple[1]) #2
print(tuple[2]) #3
print(tuple[3]) #4
print(tuple[4]) #5
print(tuple[-1]) #5 #negative indexing starts from the end
print(tuple[-2]) #4


#tuple slicing
tuple=(1, 2, 3, 4, 5)
print(tuple[0:3]) #(1, 2, 3) #slicing from index 0 to 2
print(tuple[1: 4]) #(2, 3, 4) #slicing from index 1 to 3
print(tuple[:3]) #(1, 2, 3) #slicing from the beginning to index 2
print(tuple[::-1]) #(5, 4, 3, 2, 1) #slicing with step -1 (reversing the tuple)

# #immutable nature of tuple
# tuple=(1, 2, 3, 4)
# tuple[0]=10 #TypeError: 'tuple' object does not support item assignment
# print(tuple)

#concatenation of tuples
t1=(1, 2)
t2=(3, 4)
print(t1+t2) #(1, 2, 3, 4) #concatenation of tuples
print(t1*2) #(1, 2, 1, 2) #repetition of tuple

#packing and unpacking of tuples
t=1, 2, 3 #grouping values into a tuple (packing)
#unpacking --> unpack the tuple into individual variables
a, b, c=(1, 2, 3) #unpacking the tuple into variables a, b, c
print(a) #1
print(b) #2
print(c) #3

#swap the values 
a=10
b=5
a, b=b, a #swapping the values of a and b
print(a) #5
print(b) #10

#heterogeneous tuple
t=(1.5, 2.4, 6.7, "python", True)
print(t) #(1.5, 2.4, 6.7, 'python', True) #heterogeneous tuple


#Find index of all occurrences of an element in a tuple
t = (1, 2, 3, 2, 4, 2)
x=2
for i in range(len(t)):
    if t[i] == x:
        print(i, end=" ") #1, 3, 5 #index of all occurrences of 2 in the tuple


#Find difference between consecutive elements in a tuple
t=(5,8,12,15)
differences = []
for i in range(len(t)-1):
    diff = t[i+1] - t[i]
    differences.append(diff)
print(differences) #[3, 4, 3] #difference between consecutive elements in the tuple