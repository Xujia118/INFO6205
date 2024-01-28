class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Slist:
    def __init__(self) -> None:
        self._first = None
        self._last = None
        self._n = 0
    
    def show(self):
        result = []

        cur = self._first
        while cur:
            result.append(str(cur.val))
            cur = cur.next
        
        to_print = " -> ".join(result)
        print(to_print)
        return

    # append
    def append(self, new_val):
        new_node = ListNode(new_val)

        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            # Get the last node
            last_node = self._last

            # Append the new node to the last node
            last_node.next = new_node
            
            # Update self._last pointer
            self._last = new_node
    
    # prepend
    def prepend(self, new_val):
        new_node = ListNode(new_val)

        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            # Get the first node
            first_node = self._first

            # Put the first node after the new node 
            new_node.next = first_node

            # Update self._first pointer
            self._first = new_node
            
    # popleft
    def popleft(self):
        # get the first, so we have its value and its next
        first_node = self._first
        popped_val = first_node.val

        # remove the first by pointing self._first to first.next
        self._first = first_node.next

        return popped_val
 
    # pop
    def pop(self):        
        cur = self._first

        # Deal with only one node
        if cur == self._last:
            self._first = None
            self._last = None
            return cur.val
        
        prev = None
        while cur != self._last:
            prev = cur
            cur = cur.next  

        self._last = prev
        prev.next = None
        return cur.val
    
    def peek_top(self):
        return self._last.val if self._first else None
    
    def peek_front(self):
        return self._first.val if self._last else None
    
    def empty(self):
        return self._first is None


linkedlist = Slist()

# linkedlist.append('a')
# linkedlist.append('b')
# linkedlist.append('c')
# linkedlist.append('d')
# linkedlist.append('e')
# linkedlist.append("f")
popped_left = linkedlist.popleft()
# popped_right = linkedlist.pop()
# print(popped_right)
linkedlist.show()
