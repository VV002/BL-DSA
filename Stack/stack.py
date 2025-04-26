class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def get_first(self):
        return self.stack[-1] if not self.is_empty() else "Stack is empty"
    
    def get_last(self):
        return self.stack[0] if not self.is_empty() else "Stack is empty"
    
    def length(self):
        return len(self.stack)
    
    def print_stack(self):
        print("Stack:", self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    print("Stack First Element:", stack.get_first())
    print("Stack Last Element:", stack.get_last())
    print("Stack Length:", stack.length())


if __name__ == "__main__":
    main()