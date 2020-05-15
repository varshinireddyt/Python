import weakref

class _LinkedListItem(object):
    def __init__(self, key, value, prev, next, parent):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value
        self.parent = weakref.ref(parent)

class LinkedList(object):
    '''General purpose double-linked linked list.'''

    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def add_to_back(self, key, value=None):
        '''Append item to back of list. O(1)'''
        item = _LinkedListItem(key, value, self.back, None, self)
        if self.back:
            self.back.next = item

        self.back = item

        if not self.front:
            self.front = item
        
        self.length += 1

        return item

    def remove(self, item):
        '''Remove item from list. O(1)'''
        if not isinstance(item, _LinkedListItem):
            raise Exception('item must be of class _LinkedListItem')
        if item.parent() != self:
            raise Exception('item does not belong to this list and cannot be removed')

        if item.prev:
            item.prev.next = item.next
        else:
            #no prev means it is the front
            self.front = item.next
        if item.next:
            item.next.prev = item.prev
        else:
            #no next means it is the back
            self.back = item.prev
        item.parent = None
        if not (item.prev or item.next):
            self.front = self.back = None
            self.length = 0
        else:
            self.length -= 1

    def add_to_front(self, key, value=None):
        '''Add item to front of list. O(1)'''
        item = _LinkedListItem(key, value, None, self.front, self)
        if self.front:
            self.front.prev = item
        self.front = item 
        if not self.back:
            self.back = item
        self.length += 1 
        return item

    def find_first(self, key):
        '''Returns the item for the first occurence of |key|. None if not in list. O(n)'''
        current = self.front
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def find_last(self, key):
        '''Returns the item for the last occurence of |key|. None if not in list. O(n)'''
        current = self.back
        while current:
            if current.key == key:
                return current
            current = current.prev
        return None

    def insert_after(self, item, key, value):
        '''Insert |key| in list after |item|. O(1)'''
        if not isinstance(item, _LinkedListItem):
            raise Exception('|item| must be of class _LinkedListItem')
        if item.parent() != self:
            raise Exception('|item| does not belong to this list')

        new_item = _LinkedListItem(key, value, item, item.next, self)
        if item.next:
            item.next.prev = new_item
        item.next = new_item
        if self.back == item:
            self.back = new_item
        self.length += 1 
        return new_item

    def insert_before(self, item, key, value):
        '''Insert |key|, |value| in list before |item|. O(1)'''
        if not isinstance(item, _LinkedListItem):
            raise Exception('|item| must be of class _LinkedListItem')
        if item.parent() != self:
            raise Exception('|item| does not belong to this list')

        new_item = _LinkedListItem(key, value, item.prev, item, self)
        if item.prev:
            item.prev.next = new_item
        item.prev = new_item
        if self.front == item:
            self.front = new_item
        self.length += 1 
        return new_item

    def swap(self, item1, item2):
        '''Swap places in list between |item1| and |item2|'''
        if not isinstance(item1, _LinkedListItem):
            raise Exception('|item1| must be of class _LinkedListItem')
        if not isinstance(item2, _LinkedListItem):
            raise Exception('|item2| must be of class _LinkedListItem')
        if item1.parent() != self:
            raise Exception('|item1| does not belong to this list')
        if item2.parent() != self:
            raise Exception('|item2| does not belong to this list')
        if self.front == item1:
            self.front = item2
        elif self.front == item2:
            self.front = item1
        if self.back == item1:
            self.back = item2
        elif self.back == item2:
            self.back = item1
        tmp_next = item2.next
        tmp_prev = item2.prev
        item2.next = item1.next
        if item2.next:
            item2.next.prev = item2
        item2.prev = item1.prev
        if item2.prev:
            item2.prev.next = item2
        item1.next = tmp_next
        if item1.next:
            item1.next.prev = item1
        item1.prev = tmp_prev
        if item1.prev:
            item1.prev.next = item1

    def filter(self, func):
        '''Construct a new linked list by applying |func| to all objects in list. 
        |func| must be a predicate key,val->bool.
        All items where |func| is truthy will be added to the new list. 
        If |func| == None all items will be included in the new list.
        O(n)'''
        ll = LinkedList()
        current = self.front
        while current:
            if not func or func(current.key, current.value):
                ll.add_to_back(current.key, current.value)
            current = current.next
        return ll

    def in_filter(self, func):
        '''Apply |func| to all objects in list. 
        |func| must be a predicate key,val->bool.
        All items for which |func| is falsy will be removed from the list. 
        O(n)'''
        if not func:
            return
        current = self.front
        while current:
            if not func(current.key, current.value):
                self.remove(current)
            current = current.next

    def in_map(self, func):
        '''Apply |func| to all key-value pairs in list. The result will replace
        the key-value pair. 
        |func| must be a function taking two arguments, key and value, and 
        must return a tuple (key,value)
        If |func| == None then no keys are changed.
        O(n)'''
        if not func:
            return
        current = self.front
        while current:
            tup = func(current.key, current.value)
            current.key = tup[0]
            current.value = tup[1]
            current = current.next

    def map(self, func):
        '''Contruct a new linked list by applying |func| to all key-value 
        pairs in list. 
        |func| must be a function taking two arguments, key and value, and 
        must return a tuple (key,value)
        If |func| == None all items will be included in the new list unchanged 
        O(n)'''
        ll = LinkedList()
        current = self.front
        while current:
            tup = func(current.key, current.value) if func else (current.key, current.value)
            ll.add_to_back(tup[0], tup[1])
            current = current.next
        return ll
