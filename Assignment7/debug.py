############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################
import heapq
# from Heap import *

########################################
# Nothing can be changed in class Exam
########################################


class Exam:
    def __init__(self, a: 'list of int', ans: 'list of size 2', work: 'list of size 1', show: 'bool'):
        # NOTHING CAN BE CHANGED BELOW
        self._a = a
        self._ans = ans  # [True/False, pos]
        self._work = work
        self._show = show
        s = Algorithm(self)

    # MUST USE THIS ROUTINE TO access size of a
    def __len__(self) -> 'int':
        return len(self._a)

    def __getitem__(self, i) -> 'int':
        self._work[0] += 1
        return self._a[i]

    # MUST USE THIS ROUTINE TO set ans
    def setAns_As_Heavier(self, pos) -> 'None':
        # Heavier(True) or Lighter(False)
        self._ans[0] = True
        self._ans[1] = pos

    def setAns_As_Lighter(self, pos) -> 'None':
        # Heavier(True) or Lighter(False)
        self._ans[0] = False
        self._ans[1] = pos

    # MUST USE THIS ROUTINE TO get show
    def show(self) -> 'bool':
        return self._show


################################################################################
#            Algorithm
# YOU DONT HAVE ACCESS to input array a
# Must uses s:'Exam' public function to access and fill
#         WRITE YOUR CODE HERE
################################################################################
class Algorithm:
    def __init__(self, s: 'Exam'):
        # NOTHING CAN BE CHANGED IN init
        self._s = s
        self._alg()

    ############################################################
    #                     Time:  O(n)
    #                     Space: THETA(1)
    ###########################################################
    def _alg(self) -> 'None':
        n = len(self._s)  # Number of elements in input a
        show = self._s.show()
        self.sillySolution(n)

    def sillySolution(self, n):
        # Rebuild coins array. We need the index too
        coins = [(self._s[i], i) for i in range(n)]

        # Get the first coin, second coin and the last coin.
        # It's the index 0 of a tuple
        first_coin = coins[0][0]
        last_coin = coins[-1][0]
        second_coin = coins[1][0]

        # Get min coin. Returns a tuple
        min_heap = self.buildMinHeap(coins)
        min_coin, min_idx = heapq.heappop(min_heap)

        # Get max coin. Returns a tuple
        max_heap = self.buildMaxHeap(coins)
        max_coin, max_idx = heapq.heappop(max_heap)

        # If first coin equal to last coin, then both are genuine
        if first_coin == last_coin:
            # Then if min_coin is equa to them, we need a max heap
            if min_coin == first_coin:
                print('The fake coin is heavier')
                self._s.setAns_As_Heavier(max_idx)
            # otherwise we need a min heap
            else:
                print('The fake coin is lighter')
                self._s.setAns_As_Lighter(min_idx)

        # Else one of them must be fake
        # Then we need the second coin, which now is surely genuine
        else:
            # If min_coin is lighter than this one, we know the fake is lighter
            if min_coin < second_coin:
                print('The fake coin is lighter')
                self._s.setAns_As_Lighter(min_idx)

            # Else the fake is heavier
            else:
                print('The fake coin is heavier')
                self._s.setAns_As_Heavier(max_idx)

    def buildMinHeap(self, coins):
        heapq.heapify(coins)
        return coins

    def buildMaxHeap(self, coins):
        reversed_coins = [(-coin, idx) for coin, idx in coins]
        heapq.heapify(reversed_coins)
        return reversed_coins


# Instantiate Exam class
a = [100, 100, 100, 101]
# a = [1, 1, 1, 2]
# Example initial answer, indicating lighter/heavier and the position
ans = [False, -1]
work = [0]  # Example initial work list
show = True  # Example value for the show parameter

exam_instance = Exam(a, ans, work, show)

# Instantiate Algorithm class
algo_instance = Algorithm(exam_instance)
# algo_instance._alg()
