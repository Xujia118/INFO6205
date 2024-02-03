import functools

class isHappy:
    def __init__(self, n) -> None:
        self.n = n

    def byRecursive2(self):
        visited = set()

        while self.n != 1 and self.n not in visited:
            visited.add(self.n)
            self.n = self._get_digit_square_sum2(self.n, 0)
        
        return self.n == 1

    def _get_digit_square_sum2(self, n, total):
        if n == 0:
            return total
        
        digit = n % 10
        total += digit ** 2
        n //= 10
        return self._get_digit_square_sum2(n, total)

    def byRecursive(self, operations):
        if operations == 0:
            return False

        self.n = self._get_digit_square_sum(self.n)

        if self.n == 1:
            return True

        return self.byRecursive(self.n)

    def byIterative(self):
        operations = 50

        while operations > 0:
            self.n = self._get_digit_square_sum(self.n)

            if self.n == 1:
                return True

            operations -= 1

        return False

    def _get_digit_square_sum(self, n):
        digit_square_sum = 0

        while n > 0:
            module = n % 10
            digit_square_sum += module ** 2

            n //= 10

        return digit_square_sum

    # reduce() doesn't work for n = 7, because there is no more items to reduce
    def byReduce(self):
        def helper(operations):
            if operations == 0:
                return False

            if self.n == 1:
                return True

            arr = [int(i) for i in str(self.n)]
            self.n = functools.reduce(lambda a, b: a**2 + b**2, arr)
            return helper(operations - 1)

        return helper(100)

    def byMap(self):
        def helper(operations):
            if operations == 0:
                return False

            if self.n == 1:
                return True

            arr = [int(i) for i in str(self.n)]
            arr = map(lambda x: x**2, arr)
            self.n = sum(arr)
            return helper(operations - 1)

        return helper(50)


class Solution:
    def isHappy(self, n: int) -> bool:
        check = isHappy(n)
        # return check.byMap()
        # return check.byReduce()
        # return check.byIterative()
        return check.byRecursive2()


solution = Solution()
print(solution.isHappy(19))
