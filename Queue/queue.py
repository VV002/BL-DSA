class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def delete_beginning(self):
        return self.dequeue()
    
    def delete_end(self):
        if not self.is_empty():
            return self.queue.pop()
        return "Queue is empty"
    
    def get_first(self):
        return self.queue[0] if not self.is_empty() else "Queue is empty"
    
    def get_last(self):
        return self.queue[-1] if not self.is_empty() else "Queue is empty"
    
    def length(self):
        return len(self.queue)
    
    def print_queue(self):
        print("Queue:", self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0

def main():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.delete_end()
    queue.print_queue()
    print("Queue First Element:", queue.get_first())
    print("Queue Last Element:", queue.get_last())
    print("Queue Length:", queue.length())


if __name__ == '__main__':
    main()