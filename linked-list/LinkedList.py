class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def add(self, data):
        pass

    def clear(self):
        self.head = None

    def remove(self, data):
        pass

    def printList(self):
        cur = self.head
        while cur != None:
            print(cur.data, end=", ")
            cur = cur.next


ll = LinkedList()
print(ll.getSize())

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node1.next = node2
node2.next = node3
