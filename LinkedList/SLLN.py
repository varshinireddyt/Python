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
