class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # print
    def print(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    # insertion
    def insert(self, val):
        # create a new node
        newNode = Node(val)
        # check whether it is first node or not
        if self.head is None:
            self.head = newNode
            return
        # else traverse upto last node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        # add new node
        curr.next = newNode

    # reverse
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


llist = LinkedList()
llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.insert(40)
llist.insert(50)
llist.insert(60)
llist.insert(70)
llist.insert(80)
llist.insert(90)
print('Printing Original Linked List...')
llist.print()
llist.reverse()
print('Printing Reversed Linked List...')
llist.print()
