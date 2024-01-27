############################################################
# Write code in file solution.py (Folder: HW 4)
# Post� solution.py in Canvas along with 4 screen shots that shows Leetcode has passed. We will not use screen shot to give 100
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run solution.py file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
        
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
        if self._first is None:
            return None

        # get the first, so we have its value and its next
        first_node = self._first
        popped_val = first_node.val

        # remove the first by pointing self._first to first.next
        self._first = first_node.next

        return popped_val
 
    # pop
    def pop(self):
        if self._first is None:
            return None
        
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
        return self._last.val
    
    def peek_front(self):
        return self._first.val
    
    def empty(self):
        return True if self._first is None else False
  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()
        
    def push(self, x: int) -> None:
        self._s.append(x)
        
    def pop(self) -> int:
        return self._s.pop()

    def top(self) -> int:
        return self._s.peek_top()

    def empty(self) -> bool:
        return self._s.empty()


############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()
        
    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        return self._s.popleft()
        
    def peek(self) -> int:
        return self._s.peek_front()

    def empty(self) -> bool:
        return self._s.empty()


############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
 
    def enQueue(self, value: int) -> bool:
        if self._s._len == self._K:
            return False

        self._s.append(value)
        self._s._len += 1
        return True

    def deQueue(self) -> bool:
        if self._s._len == 0:
            return False

        self._s.popleft()
        self._s._len -= 1
        return True
        
    def Front(self) -> int:
        if self._s._len == 0:
            return -1
        
        return self._s.peek_front()

    def Rear(self) -> int:
        if self._s._len == 0:
            return -1
        
        return self._s.peek_top()

    def isEmpty(self) -> bool:
        return self._s.empty()
        
    def isFull(self) -> bool:
        return self._s._len == self._K

############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
 
    def insertFront(self, value: int) -> bool:
        if self._s._len < self._K:
            self._s.prepend(value)
            self._s._len += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self._s._len < self._K:
            self._s.append(value)
            self._s._len += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self._s._len == 0:
            return False
        self._s.popleft()
        self._s._len -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self._s._len == 0:
            return False
        self._s.pop()
        self._s._len -= 1
        return True
        
    def getFront(self) -> int:
        if self._s._len == 0:
            return -1
        return self._s.peek_front()
        
    def getRear(self) -> int:
        if self._s._len == 0:
            return -1
        return self._s.peek_top()

    def isEmpty(self) -> bool:
        return self._s._len == 0
        
    def isFull(self) -> bool:
        return self._s._len == self._K