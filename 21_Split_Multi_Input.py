text = 'geeks for geeks'
# splits at space
print(text.split())

word = 'geeks, for, geeks'
# splits at ','
print(word.split(','))

word = 'geeks:for:geeks'
# split at ':'
print(word.split(':'))

word = 'CatBatSatFatOr'
# split at 3
print([word[i:i+3] for i in range(0,len(word),3)])
print()

"""
"""

word = 'geeks, for, geeks, pratap'

# maxsplit: 0
print(word.split(',',0))

# maxsplit: 4
print(word.split(',',4))

# maxsplit: 1
print(word.split(',',1))
print()

"""
"""

# multiple inputs at a time
x,y = input('Enter a two value:').split()
print('Number of Boys:',x)
print('Number of Girls:',y)
print()

"""
"""

# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

"""
"""

# taking two inputs at a time
a,b = input('Enter a two value:').split()
print('First number {} and second number {}'.format(a,b))
print()

"""
"""

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input('Enter a multiple value:').split()))
print('List of students:',x)
