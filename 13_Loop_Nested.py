"""
Syntax:

for iterator_var in sequence:
    for iterator_var in sequence:
        statements(s)
        statements(s)
"""
"""
while expression:
    while expression: 
        statement(s)
        statement(s)
"""

from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
