list_names = []              #empty list to store names

def storeName(name):         #function to store a name
    name = name.strip().title()
    if name in list_names:
        return False
    else:
        list_names.append(name)
        return True
    
def listNames():
    print('-'*30)
    for name in list_names:
        print(name)
        
    print('-'*30)

def searchName(name):
    name = name.strip().title()
    flag = False
    for item in list_names:
        if name == item:
            flag = True
            break
        if flag == True:
            print('Name is present in the list.')
        else:
            print('Name doesnt exist in the list.')

while True:
    print('Menu options')
    print('1. Enter a name')
    print('2. Search a name')
    print('3. List all names')
    print('4. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        user_input = input('Enter a name: ')
        retVal = storeName(user_input)
        if retVal == True:
            print('Name added successfully')
        else:
            print('Name exits in the list.')
    elif choice == 2:
        user_input = input('Enter the name to be searched: ')
        searchName(user_input)
    elif choice == 3:
        listNames()
    elif choice == 4:
        exit()
    else:
        print('Invalid option.')