class Node(object):
    def __init__(self, value):
        self.val=value
        self.nextnode=None
    
    def value(self):
        return self.val

    def next(self):
        return self.nextnode


class LinkedList(object):
    def __init__(self, values=[]):
        nodelist=[]
        for value in values:
            nodelist.append(Node(value))
        for i in range(1,len(nodelist)):
            nodelist[i].nextnode=nodelist[i-1]
        if len(values)==0:
            self.headnode=None
        else:
            self.headnode=nodelist[-1]


    def __len__(self):
        
        count=0
        next=self.headnode
        while next != None:
            count+=1
            next=next.next()

        return count

    def head(self):
        if self.headnode==None:
            raise EmptyListException('EmptyListException')
        return self.headnode

    def push(self, value):
        head=Node(value)
        head.nextnode= self.headnode
        self.headnode=head

    def pop(self):
        if self.headnode==None:
            raise EmptyListException('EmptyListException')
        value=self.headnode.val
        self.headnode=self.headnode.nextnode
        return value

    def reversed(self):
        values=[]
        next=self.headnode
        while next!=None:
            values.append(next.value)
            next=next.next()

        return LinkedList(values[::-1])


class EmptyListException(Exception):
    print Exception

