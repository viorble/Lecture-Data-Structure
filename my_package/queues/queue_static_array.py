# Module providing an implementation for queue, using a static array

class Queue:
    def __init__(self, max_size):
        # Creates a static array with size, max_size > 1, use list to construct static array
        if max_size <= 1:
            raise ValueError(f'Invalid size (a queue must have at least two elements): {max_size}')
        self._data = [None] * max_size
        self._max_size = max_size
        self._front = 0
        self._rear = 0
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return 'empty queue'
        result = []
        front = self._front
        if front >= self._rear:
            while front < self._max_size:
                result.append(self._data[front])
                front += 1
            front = 0
            while front < self._rear:
                result.append(self._data[front])
                front += 1
        else:
            while front < self._rear:
                result.append(self._data[front])
                front += 1        

        return f"Queue {' -> '.join(map(str, result))}"

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) == self._max_size

    def enqueue(self, value):
        if self.is_full():
            raise ValueError('The queue is already full!')
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._max_size
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        value = self._data[self._front]
        self._front = (self._front + 1) % self._max_size
        self._size -= 1
        return f"{value} dequeued from the queue"

if __name__ == "__main__":
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue)
    queue.enqueue(4)
    print(queue)
    print(queue.dequeue())
    queue.enqueue(5)
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)