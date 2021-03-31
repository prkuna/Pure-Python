# function with main
def getInteger():
    result = int(input('Enter integer: ')
                 return result

def Main():
    print('Started')

    """ calling the getInteger function and
        storing its returned value in the output variable """
    output = getInteger()
    print(output)

""" Now we are required to tell python
    for 'Main' function existence """
if _name_ == '_main_':
    mian()
