class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
class Slist:
    def __init__(self) -> None:
        self._first = None
        self._last = None
        self._len = 0

    # show
    def show(self):
        if self._first is None:
            return ''

        result = []
        cur = self._first
        
        while cur:
            result.append(cur.val)
            cur = cur.next
        
        return " -> ".join(result)

    # append
    def append(self, new_val):
        new_node = ListNode(new_val)

        if self._first is None:
            self._first = new_node
        else:
            self._last.next = new_node
        self._last = new_node
        
    # prepend
    def prepend(self, new_val):
        new_node = ListNode(new_val)

        if self._first is None:
            self._last = new_node
        else:
            new_node.next = self._first
        self._first = new_node
 
    # pop
    def pop(self):
        prev, cur = None, self._first
        cur = self._first

        if self._first == self._last:
            self._first = 0
            self._last = 0
            return cur.val

        while cur.next:
            prev = cur
            cur = cur.next
        
        self._last = prev
        prev.next = None
        return cur.val
        
    # popleft
    def popleft(self):
        first_val = self._first.val
        self._first = self._first.next
        return first_val
        
    # get_end
    def get_end(self):
        return self._last.val if self._last else None
        
    # get_front
    def get_front(self):
        return self._first.val if self._first else None
        
    # isEmpty
    def check_empty(self):
        return self._first is None

slist = Slist()
# slist.append('a')
# slist.append('b')
# slist.append('c')
# slist.append('d')
# slist.append('e')




