class MinStack:

    #https://leetcode.com/problems/min-stack/
    def __init__(self):
        self.stack = []


    def push(self, x):
        """
        if stack is empty, set the cur_min as x+1 to garantee
        we can set the updated min x as x when do the min(x, x+1)
        """
        if self.getMin() == None:
            cur_min = x+1
        else:
            cur_min = self.getMin()

        #cur_min = x+1 if self.getMin() == None else self.getMin()

        self.stack.append((x, min(x, cur_min)))

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()

    def top(self):
        print self.stack[-1]
        return self.stack[-1][0] if self.stack else None


    def getMin(self):
        return self.stack[-1][1] if self.stack else None



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print obj.stack
obj.push(-2)
print obj.stack
obj.push(0)
print obj.stack
obj.push(-3)
print obj.stack
obj.pop()
print obj.top()
print obj.getMin()
