class Stack:

    def __init__(self, optional_max_length = -1):
        self.stack_list = []
        self.max_length = optional_max_length

    def __len__(self):
        return len(self.stack_list)

    def pop(self):
        return self.stack_list.pop()

    def push(self, item):
        
        if len(self.stack_list) == self.max_length:
            return False

        self.stack_list.append(item)
        return True


bounded_stack = Stack(4)
unbounded_stack = Stack()


values_to_push = list(range(1, 9))
print("Pushing values 1 through 8 to each stack")
for i in values_to_push:
    bounded_stack.push(i)
    unbounded_stack.push(i)


print("Popping twice")
for i in range(2):
    bounded_stack.pop()
    unbounded_stack.pop()


values_to_push = list(range(10, 50, 10))
print(f"Pushing values to each stack: {values_to_push}")
for i in values_to_push:
    bounded_stack.push(i)
    unbounded_stack.push(i)


print(f"Bounded stack (max_length={bounded_stack.max_length}) contents:")
while len(bounded_stack) > 0:
    print(f"  {bounded_stack.pop()}")
print("Unbounded stack contents:")
while len(unbounded_stack) > 0:
    print(f"  {unbounded_stack.pop()}")