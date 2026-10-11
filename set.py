#set --> Collection of elements, but with properties include
#not maintain inserted order
#not allow duplicate values
#heterogeneous
#mutable
#set is represented by {} or set() constructor

#creating set
s={1,2,3,4,5}
print(s) #{1, 2, 3, 4, 5}
print(type(s)) #<class 'set'>

#duplicate values are not allowed in set
s={1,2,1,3,4}
print(s) #duplicate values are not allowed

#Declaring empty set
s={} #this is not empty set, it is dictionary
print(type(s)) #<class 'dict'>

#how can i create empty set
s=set() #this is empty set
print(s) #set()

#add element in set
s={1,2,3}
s.add(4) #add() method is used to add element in set
print(s) #{1, 2, 3, 4}

#adding multiple elements in set
s={1,2,3}
s.update([4,5,6]) #update() method is used to add multiple elements in set
print(s) #{1, 2, 3, 4, 5, 6}

#deleting element from set
s={1,2,3,4,5}
s.remove(3) #remove() method is used to delete element from set
print(s) #{1, 2, 4, 5}

#if we try to delete element which is not present in set, it will raise error
s={1,2,3,4,5}
s.discard(6) #discard() method is used to delete element from set, but if element is not present in set, it will not raise error
print(s) #{1, 2, 3, 4, 5}

#deleting random element from set
s={1,2,3,4,5}
s.pop() #pop() method is used to delete random element from set
print(s) #{2, 3, 4, 5} #random element is deleted from set

#deleting all elements from set
s={1,2,3,4,5}
s.clear() #clear() method is used to delete all elements from set
print(s) #set() #all elements are deleted from set

#combining two sets
a={1,2,3}
b={4,5,6}
c=a.union(b) #union() method is used to combine two sets
d=b.union(a) #union() method is used to combine two sets
print(c) #{1, 2, 3, 4, 5, 6} 
print(d) #{1, 2, 3, 4, 5, 6}

#finding common elements in two sets
a={1,2,3}
b={2,3,4}
print(a.intersection(b)) #intersection() method is used to find common elements in two sets

print(b.intersection(a)) #intersection() method is used to find common elements in two sets

print(a.difference(b)) #difference() method is used to find elements which are present in set a but not in set b

print(b.difference(a)) #difference() method is used to find elements which are present in set b but not in set a

print(a.symmetric_difference(b)) #symmetric_difference() method is used to find elements which are present in set a or set b but not in both sets

print(b.symmetric_difference(a)) #symmetric_difference() method is used to find elements which are present in set a or set b but not in both sets
