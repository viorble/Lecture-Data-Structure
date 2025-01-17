from collections import deque

class RecentCounter:
    
    def __init__(self):
        self.queue = deque()
        
    def ping(self, t):
        queue = self.queue
        start = t - 3000
        queue.append(t)
        
        while queue and queue[0] < start:
            queue.popleft()
        
        return len(queue)
    
    
obj = RecentCounter()
print(obj.ping())
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))

