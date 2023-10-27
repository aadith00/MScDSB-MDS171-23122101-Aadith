class stacking:
    
    def __init__(self) -> None:
        self.stack = []

    def push(self,value):
        self.stack.append(value)
        print(self.stack)

    def pop(self,value):
        self.stack.pop(value)
        print(self.stack)

    def display(self):
        for items in self.stack:
            print(items)

    def size(self):
        print(len(self.stack))

    def top_item(self):
        print(self.stack[len(self.stack)-1])

    def check(self):
        if len(self.stack) == 0:
            print('The stack is empty.')
        else:
            print('The stack is not empty.')

stack_1 = stacking()
stack_1.push('Apple')
stack_1.push('Orange')
stack_1.push('Mango')
stack_1.pop(2)
stack_1.display()
stack_1.size()
stack_1.top_item()
stack_1.check()

while True:
    print('1. Push a value.')
    print('2. Pop a value.')
    print('3. Print items in the stack.')
    print('4. Print size of the stack.')
    print('5. Display top-most item in the stack.')
    print('6. Check if the stack is empty.')
    print('7. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        value = input('Enter the value to be added into the stack: ')
        stack_1.push(value)
        print(stack_1)
    elif choice == 2:
        value = int(input('Enter the index number of item to be removed: '))
        stack_1.pop(value)
        print(stack_1)
    elif choice == 3:
        stack_1.display()
    elif choice == 4:
        stack_1.size()
    elif choice == 5:
        stack_1.top_item()
    elif choice == 6:
        stack_1.check()
    elif choice == 7:
        exit(1)
    else:
        print('Invalid option.')