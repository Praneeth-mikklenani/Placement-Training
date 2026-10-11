n= int(input("Enter n:"))
for i in range(n):
    val=1
    for j in range(i+1):
        print(val,end=" ")
        val=val*(i-j)//(j+1)
    print()    


nums=[1,2,3,4,5]
print(nums[0:3])
print(nums[:4])
print(nums[0:])
print(nums[0:5:2])


#Check whether list is in ascending order.
#1 2 3 4 5
#current element is less than next element then it is in ascending order.
#repeat the process for all the elements in the list.
nums=[11,12,13,14,15]
is_sorted=True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")


#Remove duplicates in list.
#create a new list and add all the unique elements from the original list to the new list.
nums=[1,2,2,3,1,4,4,5]
result=[]
for num in nums:
    if num not in result:
        result.append(num)
print(result)


#You are given with two lists find common elements between two lists
list1=[1,2,3,4]
list2=[3,4,5,6]
result=[]
for i in list1:
    if i in list2:
        result.append(i)
print(result)
