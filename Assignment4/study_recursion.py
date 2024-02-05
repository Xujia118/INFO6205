from collections import deque

class Study:
    def __init__(self) -> None:
        pass

    # Input a number and print digit in order
    def asis_iterative(self, n):
        digits_holder = deque()

        while n > 0:
            module = n % 10
            digits_holder.append(module)
            n //= 10

        result = 0
        i = 0
        while digits_holder:
            result += digits_holder.popleft() * 10 ** i
            i += 1
        return result

    def asis_recursive(self, n, result=0):
        def helper(n, s):
            if n == 0:
                return s

            s.append(n % 10)
            return helper(n // 10, s)
        
        s = []
        digits_holder = helper(n, s)
        digits_holder = deque(digits_holder)

        result = 0
        i = 0
        while digits_holder:
            result += digits_holder.popleft() * 10 ** i
            i += 1
        return result


    def asis_reverse_iterative(self, n):
        s = 0

        while n > 0:
            module = n % 10
            s = s * 10 + module
            n //= 10

        return s
    
    def asis_reverse_recursive(self, n):
        def helper(n, s):
            if n == 0:
                return s
            
            last_digit = n % 10
            s = s * 10 + last_digit
            return helper(n // 10, s)
        
        s = 0
        return helper(n, s)

    # Input a number and print digit in reverse order
    def printR(self, n, reverse: "bool"):
        if n == 0:
            print(0)
            return

        return self._printR(n)
    
    def _printR(self, n):
        if n == 0:
            return

        module = n % 10
        print(module)
        self._printR(n // 10)


    # def printR(self, n, reverse: "bool"):
    #     if n == 0:
    #         print(0)
    #         return
    #     else:
    #         self._printR(n)


    # def _printR(self, n):
    #     if n == 0:
    #         return

    #     module = n % 10
    #     print(module)
    #     self._printR(n // 10)


n = 1986
study = Study()
# print(study.asis_iterative(n))
# print(study.asis_recursive(n))
# print(study.asis_reverse_iterative(n))
# print(study.asis_reverse_recursive(n))
study.printR(n, reverse=True)
