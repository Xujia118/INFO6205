class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return self.head
        
        cur = self.head
        while cur.next:
            cur = cur.next
        
        cur.next = new_node
        return self.head
    
    def reverseI(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        prev, cur = None, self.head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        self.head = prev # Update self.head, it's global.
        return prev
    
    def reverseR(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        def reverse_helper(prev, cur):
            if cur is None:
                return prev
            
            next_node = cur.next
            cur.next = prev
            return reverse_helper(cur, next_node)

        self.head = reverse_helper(None, self.head)
        return self.head
        # Don't do return reverse_helper(None, self.head). 
        # That will leave self.head not updated.

    def show(self):
        result = []

        cur = self.head
        while cur:
            result.append(str(cur.val))
            cur = cur.next
        
        return '->'.join(result)
    
ll = LinkedList()
ll.append('a')
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('e')

# ll.reverseI()
ll.reverseR()
print(ll.show())


