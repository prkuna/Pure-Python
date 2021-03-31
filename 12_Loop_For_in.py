"""
Syntax:

for iterator_var in sequence:
    statements(s)
"""

# Iterating over a list
print('List Iteration')
l = ['geeks','for','geeks']
for i in l:
    print(i)

# Iterating over a Tuple (immutable)
print('\nTuple Iteration')
t = ('geeks','for','geeks')
for i in t:
    print(i)

# Iteration over a String
print('\nString Iteration')
s = 'Geeks'
for i in s:
    print(i)

# Iteration over dictionary
print('\nDictionary Iteration')
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print('%s %d' %(i,d[i]))
