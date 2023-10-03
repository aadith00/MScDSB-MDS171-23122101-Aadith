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