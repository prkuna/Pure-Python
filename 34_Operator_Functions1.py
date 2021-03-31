# importing operator module 
import operator

# Initializing variables
a = 4  
b = 3

# 1. add(a, b) :- This functions returns addition of the given arguments.
# Operation – a + b.
# using add() to add two numbers
print ('The addition of numbers is : ',end='');
print (operator.add(a, b))


# 2. sub(a, b) :- This functions returns difference of the given arguments.
# Operation – a – b.
# using sub() to subtract two numbers
print ('The difference of numbers is : ',end='');
print (operator.sub(a, b))

# 3. mul(a, b) :- This functions returns product of the given arguments.
# Operation – a * b.
# using mul() to multiply two numbers
print ("The product of numbers is :",end="");
print (operator.mul(a, b))

# 4. truediv(a,b) :- This functions returns division of the given arguments.
# Operation – a / b.
# using truediv() to divide two numbers
print ("The true division of numbers is : ",end="");
print (operator.truediv(a,b))

# 5. floordiv(a,b) :- This functions also returns division of the given arguments.
# But the value is floored value i.e. returns greatest small integer.
# Operation – a // b.
# using floordiv() to divide two numbers
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(a,b))

# 6. pow(a,b) :- This functions returns exponentiation of the given arguments.
# Operation – a ** b.
# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(a,b))

# 7. mod(a,b) :- This functions returns modulus of the given arguments.
# Operation – a % b.
# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ",end="");
print (operator.mod(a,b))

# 8. lt(a, b) :- This function is used to check if a is less than b or not.
# Returns true if a is less than b, else returns false.
# Operation – a < b.
# using lt() to check if a is less than b
if(operator.lt(a,b)):
       print ("4 is less than 3")
else : print ("4 is not less than 3")

# 9. le(a, b) :- This function is used to check if a is less than or equal to b or not.
# Returns true if a is less than or equal to b, else returns false.
# Operation – a <= b.
# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
       print ("4 is less than or equal to 3")
else : print ("4 is not less than or equal to 3")

# 10. eq(a, b) :- This function is used to check if a is equal to b or not.
# Returns true if a is equal to b, else returns false.
# Operation – a == b.
# using eq() to check if a is equal to b
if (operator.eq(a,b)):
       print ("4 is equal to 3")
else : print ("4 is not equal to 3")

# 11. gt(a,b) :- This function is used to check if a is greater than b or not.
# Returns true if a is greater than b, else returns false.
# Operation – a > b.
# using gt() to check if a is greater than b
if (operator.gt(a,b)):
       print ("4 is greater than 3")
else : print ("4 is not greater than 3")

# 12. ge(a,b) :- This function is used to check if a is greater than or equal to b or not.
# Returns true if a is greater than or equal to b, else returns false.
# Operation – a >= b.
# using ge() to check if a is greater than or equal to b
if (operator.ge(a,b)):
       print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")

# 13. ne(a,b) :- This function is used to check if a is not equal to b or is equal.
# Returns true if a is not equal to b, else returns false.
# Operation – a != b.
# using ne() to check if a is not equal to b
if (operator.ne(a,b)):
       print ("4 is not equal to 3")
else : print ("4 is equal to 3")
