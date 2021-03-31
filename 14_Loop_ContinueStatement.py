# It returns the control to the beginning of the loop.

# print all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter:',letter)
    var = 10
