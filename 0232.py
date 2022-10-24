class MyQueue(object):
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)        

    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        this = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return this
        

    def peek(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        this = self.stack2.pop()
        self.stack2.append(this)

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return this
        

    def empty(self):
        return len(self.stack1) == 0