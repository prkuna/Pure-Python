# importing operator module 
import operator

# Initializing list
li = [1, 5, 6, 7, 8]

# printing original list 
print ("The original list is : ",end="")
for i in range(0,len(li)):
    print (li[i],end=" ")

print ("\r")

# 1. setitem(ob, pos, val) :- This function is used to assign the value at a
# particular position in the container. 
# Operation – ob[pos] = val
# using setitem() to assign 3 at 4th position
operator.setitem(li,3,3)

# printing modified list after setitem()
print ("The modified list after setitem() is : ",end="")
for i in range(0,len(li)):
    print (li[i],end=" ")  

print ("\r")

# 2. delitem(ob, pos) :- This function is used to delete the value at a
# particular position in the container. 
# Operation – del ob[pos]
# using delitem() to delete value at 2nd index
operator.delitem(li,1)
  
# printing modified list after delitem()
print ("The modified list after delitem() is : ",end="")
for i in range(0,len(li)):
    print (li[i],end=" ")
  
print ("\r")

# 3. getitem(ob, pos) :- This function is used to access the value at a
# particular position in the container. 
# Operation – ob[pos]
# using getitem() to access 4th element
print ("The 4th element of list is : ",end="")
print (operator.getitem(li,3))

# 4. setitem(ob, slice(a,b), vals) :- This function is used to set the values
# in a particular range in the container. 
# Operation – obj[a:b] = vals
# using setitem() to assign 2,3,4 at 2nd,3rd and 4th index
operator.setitem(li,slice(1,4),[2,3,4])
  
# printing modified list after setitem()
print ("The modified list after setitem() is : ",end="")
for i in range(0,len(li)):
    print (li[i],end=" ")
  
print ("\r")

# 5. delitem(ob, slice(a,b)) :- This function is used to delete the values
# from a particular range in the container. 
# Operation – del obj[a:b]
# using delitem() to delete value at 3rd and 4th index
operator.delitem(li,slice(2,4))
  
# printing modified list after delitem()
print ("The modified list after delitem() is : ",end="")
for i in range(0,len(li)):
    print (li[i],end=" ")
  
print ("\r")

# 6. getitem(ob, slice(a,b)) :- This function is used to access the values in
# a particular range in the container. 
# Operation – obj[a:b]
# using getitem() to access 1st and 2nd element
print('The 1st and 2nd element of list is : ',end='')
print(operator.getitem(li,slice(0,2)))

# 7. concat(ob1,obj2) :- This function is used to concatenate two containers. 
# Operation – obj1 + obj2

# Initializing string 1
s1 = "geeksfor"
  
# Initializing string 2
s2 = "geeks"

# using concat() to concatenate two strings
print ("The concatenated string is : ",end="")
print (operator.concat(s1,s2))

# 8. contains(ob1,obj2) :- This function is used to check if obj2 in present in obj1. 
# Operation – obj2 in obj1
# using contains() to check if s1 contains s2
if (operator.contains(s1,s2)):
       print ("geeksfor contains geeks")
else : print ("geeksfor does not contain geeks")

