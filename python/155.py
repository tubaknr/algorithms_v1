# min stack
# design a stack that supports push, pop, top, and retrieving the minimum element n constant time. 
# input: ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
# and input cont: [[],[-2],[0],[-3],[],[],[],[]] 
# output: [null, null, null, null, -3, null, 0, -2]
# push(val): Stack'e bir eleman ekler.
# pop(): Stack'ten en üstteki elemanı çıkarır.
# top(): Stack'in en üstündeki elemanı döndürür.
# getMin(): O(1) sürede stack içindeki en küçük elemanı döndürür.


class MinStack:
    def __init__(self):
        self.stack = [] # tüm elemanları saklar.
        self.minStack = [] # o ana kadar gördüğümüz en küçük elemanı saklar.

    def push(self, val):
        self.stack.append(val)
        # eğer minStack boş değilse, yeni eklenen değeri önceki minimumla kıyasla. 
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
print(obj.top())
print(obj.getMin())








