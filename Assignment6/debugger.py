############################################################
# L0322.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# All imports
###########################################################
from typing import List
from time import process_time


class Solution:
    # YOU CANNOT CHANGE THIS INTERFACE
    # LEETCODE INTERFACE
    def coinChange(self, coins: List[int], amount: int) -> int:
        # YOU CANNOT CHANGE ANYTHING IN THIS PROCEDURE
        work = [0]
        changes = []  # If change cannot be given, you must put -1 in changes[0]
        show = False
        p = L0322(coins, amount, changes, work, show)
        num_change = len(changes)
        if (num_change == 1):
            if (changes[0] == -1):
                num_change = -1
        return num_change


class L0322:
    def __init__(self, coins: List[int], amount: 'int', changes: 'list of int', work: 'List of size 1', show: 'boolean'):
        # NOTHING CAN BE CHANGED
        self._d = coins
        self._n = amount
        self._ans = changes
        self._work = work
        self._show = show
        # YOU MUST GENERATE V table and k table
        self._v = []
        self._k = []
        # You can have any number of data structures here
        # MUST WRITE TWO ROUTINES
        self._alg()
        self._get_solution()

    def _increment_work(self):
        self._work[0] = self._work[0] + 1

    ############################################################
    # WRITE CODE BELOW
    ###########################################################

    ############################################################
    # TIME (n * k ) = O(n)
    # SPACE O(n)
    ############################################################

    def _alg(self):
        print("WRITE CODE")

        self._v = [float('inf')] * (self._n + 1)
        self._v[0] = 0
        self._k = [0] * (self._n + 1)

        for i in range(1, self._n + 1):
            min_coins = float('inf')
            first_coin = None

            for coin in self._d:
                if coin <= i:
                    if 1 + self._v[i - coin] < min_coins:
                        min_coins = 1 + self._v[i - coin]
                        first_coin = coin
        
            self._v[i] = min_coins
            self._k[i] = first_coin

        # print(self._v)
        # print(self._k)

        # Now this is correct!
        # self._v = [0, 1, 2, 1, 1, 2, 2]
        # self._k = [0, 1, 1, 3, 4, 1, 3]
            
        # Population self._ans with the optimal solution
        self._get_changes()   

    # Populate self._ans with the optimal solution
    def _get_changes(self):
        if self._v[self._n] != float('inf'):
            amount = self._n
            while amount > 0:
                coin = self._k[amount]
                self._ans.append(coin)
                amount -= coin
        else:
            self._ans.append(-1)  # No optimal solution found


    ############################################################
    # NOTHING CAN BE CHANGED IN THIS ROUTINE BELOW
    ###########################################################
    def _get_solution(self):
        if (self._show):
            a = []
            for i in range(self._n + 1):
                a.append(i)
            print(a)
            print(self._v)
            print(self._k)
        if (self._n < 1000):
            for i in range(self._n + 1):
                if (self._show):
                    print("minimum change for", i,
                          "cents can be achieved using", self._v[i], "coins.")
                self._get_solution1(i)
        else:
            self._get_solution1(self._n)

    ############################################################
    # TIME O(n)
    # SPACE THETA(1)
    # How will you give change for p cents
    # WRITE CODE BELOW
    ############################################################
    def _get_solution1(self, p: 'int'):
        print("WRITE CODE")

        coins = self._d
        amount = p

        while amount > 0:
            for coin in coins:
                if self._v[amount] == 1 + self._v[amount - coin]:
                    self._k.append(coin)
                    amount -= coin
                    break

amount = 6
coins = [1, 3, 4]
solution = Solution()
print(solution.coinChange(coins, amount))
# p = L0322(coins, amount, changes=[], work=[0], show=False)
# p._get_solution1(amount)
# p._alg()
