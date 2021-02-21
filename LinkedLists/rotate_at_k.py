# concept:
'''
We'll split linked list into two parts from kth node.
We're using zero index i.e., k=4 will be 3rd node of linked list.
'''


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

    # rotation at kth node
    def rotate(self, k):
        if k == 0:
            return head
        # else
        curr = self.head
        for i in range(k-1):
            curr = curr.next
        # store next node
        next = curr.next
        # set head to next i.e., kth node will be head
        oldHead = self.head
        self.head = next
        # set kth node to None
        curr.next = None
        # traverse second linked list
        while next.next:
            next = next.next
        next.next = oldHead


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
llist.rotate(4)
print('Printing Rotated Linked List...')
llist.print()
