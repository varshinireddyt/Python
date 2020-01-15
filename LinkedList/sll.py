# Single Linked List
class SLLNode:

    def __init__(self,data):
        self.data = data
        self.next = None  #Node we're doesn't yet point

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL object: head={}".format(self.head)

    def is_empty(self):
        """Returns True if the linked list is empty"""
        return self.head is None

    def add_front(self, new_data):
        """ADD a Node whose data is new data to the front of the linked list"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Traverses the Linked List and returns the integer value represents the number of nodes in the Linked List
        The Time Complexity is O(n)
        Every node in the list must be visited"""
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """It returns True if the data exists and False if not found"""
        if self.head is None:
            return "Linked List is empty"

        current = self.head
        while current is not None:
            # Data matches
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False


    def remove(self, data):
        if self.head is None:
            return "Linked List is empty"

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next == None:
                    return "A node with that data is not in the list"
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())