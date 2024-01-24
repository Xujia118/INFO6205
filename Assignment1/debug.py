from typing import List
from time import process_time
import math

########################################
#Nothing can be changed in class Solution
# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
########################################
class Solution:
    #YOU CANNOT CHANGE THIS INTERFACE
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        work = [0]
        p = L0977("NSquareTime_1_Space",nums,ans,work,False)
        # p = L0977("NlognTime_N_Space",nums,ans,work,False)
        # p = L0977("NTime_1_Space",nums,ans,work,False)
        return ans

########################################
#Nothing can be changed in class L0977
########################################
class L0977:
    def __init__(self,alg:'string',a:List[int], ans:List[int], work:'List of size 1', show:'bool'):
        self._a = a ;
        self._ans = ans ;
        self._work = work ;
        self._show = show ;
        algb = AlgL0977(self,alg,ans,show)

    def size(self)->'int':
        return len(self._a)

    def get(self,i:'int'):
        self._work[0] = self._work[0] + 1
        return self._a[i]

    def increment_work(self,i:'int'):
        self._work[0] = self._work[0] + i

########################################
# WRITE CLASS AlgL0977
#YOU CAN HAVE ANY NUMBER OF PRIVATE VARIABLES and FUNCTIONS
########################################
class AlgL0977():
    def __init__(self,h:'L0977',alg:'string', ans:List[int],show:'bool'):
        self._h = h 
        self._ans = ans 
        self._show = show 
        if (alg == "NSquareTime_1_Space"):
            self._alg_NSquareTime_1_Space()
        elif (alg == "NlognTime_N_Space"):
            self._alg_NlognTime_N_Space()
        elif (alg == "NTime_1_Space"):
            self._alg_NTime_1_Space()
        else:
            assert(False)

    ########################################
    #   WRITE YOUR CODE BELOW
    #######################################

    ########################################
    # TIME:O(N^2)
    # Space:O(1)
    #########################################
    def _alg_NSquareTime_1_Space(self):
        n = self._h.size();

        result = []
        for i in range(n):
            result.append(self._h.get(i) ** 2)
        
        self._selectSort(result)
        self._ans.extend(result)
    
    def _selectSort(self, arr):
        for i in range(len(arr)):
            min_index = i
            
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            
            arr[i], arr[min_index] = arr[min_index], arr[i]
        
        return arr

solution = Solution()
nums = [-4,-1,0,3,10]
nums = [-7,-3,2,3,11]
print(solution.sortedSquares(nums))