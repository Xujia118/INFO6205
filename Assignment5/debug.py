############################################################
# L0162.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################
############################################################
# All imports
###########################################################
from typing import List

############################################################
# You cannot change anything in Solution
###########################################################


class Solution:
    def findPeakElement(self, nums: List[int]) -> 'int':
        work = [0]
        ans = [-1]
        show = False
        if (False):
            b = L0162(nums, ans, work, show, "n time constant space")
        if (True):
            b = L0162(nums, ans, work, show, "logn time logn space")
        if (False):
            b = L0162(nums, ans, work, show, "logn time constant space")
        return ans[0]

############################################################
# You cannot change anything in L0162
###########################################################


class L0162:
    def __init__(self, a: List[int], ans: 'list of size 1', work: 'list of size 1', show: 'bool', alg: 'string') -> None:
        self._a = a
        self._ans = ans
        self._work = work
        self._show = show
        self._l = len(a)
        Algorithm(self, alg)

    def __len__(self):
        return self._l

    def __getitem__(self, i: 'int') -> 'int':
        assert (i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1
        return self._a[i]

    def set_ans_index(self, i: 'int') -> 'none':
        assert (i >= 0 and i < self._l)
        self._ans[0] = i

    def show(self) -> 'bool':
        return self._show


class Algorithm:
    def __init__(self, s: 'L0162', alg: 'string') -> None:
        self._s = s

        if (alg == "n time constant space"):
            self._n_time_constant_space()
        elif (alg == "logn time logn space"):
            self._logn_time_logn_space()
        elif (alg == "logn time constant space"):
            self._logn_time_constant_space()
        else:
            assert (False)

    def show(self) -> 'bool':
        return self._s.show()

    ########################################
    # WRITE CODE BELOW
    #########################################

    ########################################
    # TIME:O(N)
    # Space:THETA(1)
    #
    #########################################

    def _n_time_constant_space(self):
        n = len(self._s)
        max_num = float('-inf')
        max_index = None
        cur_index = 0

        while cur_index < n:
            cur_num = self._s.__getitem__(cur_index)

            if cur_num > max_num:
                max_num = cur_num
                max_index = cur_index

            cur_index += 1

        if max_index != float('-inf'):
            self._s._ans[0] = max_index
        else:
            self._s._ans[0] = -1


    ########################################
    # TIME:O(log n)
    # Space:O(logn )
    #########################################
    def _logn_time_logn_space(self) -> 'None':
        n = len(self._s)

        def findPeak(left, right):
            if left == right:
                self._s._ans[0] = left
                return
            
            mid = (left + right) // 2

            if self._s.__getitem__(mid) < self._s.__getitem__(mid + 1):
                return findPeak(mid + 1, right)
            else:
                return findPeak(left, mid)
        
        return findPeak(0, n - 1)


    ########################################
    # TIME:O(log N)
    # Space:THETA(1)
    #########################################
    def _logn_time_constant_space(self) -> 'None':
        n = len(self._s)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if (mid == 0 or self._s.__getitem__(mid) > self._s.__getitem__(mid - 1)) and \
                    (mid == n - 1 or self._s.__getitem__(mid) > self._s.__getitem__(mid + 1)):
                self._s._ans[0] = mid
                return 
            elif mid > 0 and self._s.__getitem__(mid) < self._s.__getitem__(mid - 1):
                right = mid - 1
            else:
                left = mid + 1
        
        self._s._ans[0] = -1


nums = [1, 2, 3, 1]
nums = [1, 2, 1, 3, 5, 6, 4]
solution = Solution()
print(solution.findPeakElement(nums))
