class Solution:
    def __init__(self):
        self.work = 0
        
    def getRoot(self, n):
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 <= n and (mid + 1) ** 2 > n:
                return mid
            elif mid ** 2 < n:
                left = mid
            else:
                right = mid
            
            self.work += 1
        
    def get_work(self):
        return self.work

n = 99
solution = Solution()
root = solution.getRoot(n)
steps = solution.get_work()
print(f"Integer root of {n} is", root)
print(f"It took {steps} steps")