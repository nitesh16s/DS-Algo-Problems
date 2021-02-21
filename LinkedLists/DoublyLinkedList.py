class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f'Node Class for doubly linked list'


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr

    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def printList(self):
        curr = self.head
        while curr.next:
            print(curr.val)
            curr = curr.next
        print(curr.val)
        print('Reverse printing: ')

        while curr != None:
            print(curr.val)
            curr = curr.prev
        

dll = DoublyLinkedList()
dll.insertAtEnd(3)
dll.insertAtEnd(4)
dll.insertAtEnd(5)
dll.insertAtEnd(6)
dll.insertAtEnd(7)

dll.insertAtBegin(2)
dll.insertAtBegin(1)
dll.insertAtBegin(0)

dll.printList()