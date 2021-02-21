class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SingleLinkedList:

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
        curr = newNode

    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    # def insertAtKthPosition(self, data, position):
    #     newNode = Node(data)
    #     length = 0
    #     if self.head is None:
    #         self.head = newNode
    #     curr = self.head
    #     while curr.next and position >= 2:
    #         len
    #         curr = curr.next
    #         position -= 1
    #         print('tr', curr.val, position)
    #         if curr is None:
    #             raise IndexError('Invalid position')
    #     newNode.next = curr.next
    #     curr.next = newNode
    #     curr = newNode

    def printList(self):
        while self.head:
            print(self.head.val)
            self.head = self.head.next


sll = SingleLinkedList()
sll.insertAtEnd(3)
sll.insertAtEnd(4)
sll.insertAtEnd(6)

sll.insertAtBegin(2)
sll.insertAtBegin(1)
sll.insertAtBegin(0)

# sll.insertAtKthPosition(5, 10)

sll.printList()
