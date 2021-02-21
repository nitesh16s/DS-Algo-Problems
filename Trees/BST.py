class BinarySearchTree:

    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_node(self, data):
        """
        If data already present
        """
        if data == self.data:
            return 'Node already present'

        """
        If data is less than root value
        than insert
        """
        if data < self.data:
            if self.left_child:
                self.left_child.add_node(data)
            else:
                self.left_child = BinarySearchTree(data)

        else:
            if self.right_child:
                self.right_child.add_node(data)
            else:
                self.right_child = BinarySearchTree(data)

    def remove_node(self, data):
        if not self.data:
            return None
        if self.data > data:
            self.left_child = self.remove_node(data)
        elif self.data < data:
            self.right_child = self.remove_node(data)
        else:
            pass