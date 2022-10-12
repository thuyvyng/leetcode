class MyQueue(object):
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(1)
        

    def pop(self):
        for _ in self.stack1:
            self.stack2.append(self.stack1.pop())
        this = self.stack2.pop()

        for _ in self.stack2:
            self.stack1.append(self.stack2.pop())
        return this
        

    def peek(self):
        for _ in self.stack1:
            self.stack2.append(self.stack1.pop())
        this = self.stack2.pop()
        self.stack1.append(this)

        for _ in self.stack2:
            self.stack1.append(self.stack2.pop())
        return this
        

    def empty(self):
        return len(self.stack1)  == 0