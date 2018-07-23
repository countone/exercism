class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity=capacity
        self.buffer=[]

    def read(self):

        if not self.buffer:
            raise BufferEmptyException("BufferEmptyException")
        else:
            self.out= self.buffer[0]
            del(self.buffer[0])
            return self.out


    def write(self, data):
        
        if len(self.buffer)<self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException("BufferFullException")

    def overwrite(self, data):
        if len(self.buffer)==self.capacity:
            del(self.buffer[0])
            self.buffer.append(data)
        else:
            self.buffer.append(data)

    def clear(self):
        self.buffer=[]
