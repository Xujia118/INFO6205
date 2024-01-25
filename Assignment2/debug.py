############################################################
# L0204.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
# NOTHING CAN BE CHANGED
# 204. Count Primes
# https://leetcode.com/problems/count-primes/
############################################################
class Solution:
    def countPrimes(self, n: int) -> int:
        list = []
        work = [0]
        if True:
            L0204(n, list, work, "up_to_prime")
        if False:
            L0204(n, list, work, "sieve_of_eratosthenes")
        return len(list)


############################################################
#  L0204 class
############################################################
class L0204:
    def __init__(
        self, n: "int", prime_number_list: "list", work: "list of size 1", alg: "string"
    ):
        self._n = n
        self._prime_number_list = (
            prime_number_list  # You need to append this using _append_prime_number
        )
        self._work = work  # You need to increment using _increment_work_done()
        if alg == "up_to_prime":
            self.up_to_primes()
        elif alg == "sieve_of_eratosthenes":
            self.sieve_of_eratosthenes()
        else:
            assert False

    ############################################################
    # All work done goes through this routine.
    # Nothing can be changed
    ###########################################################
    def _increment_work_done(self):
        self._work[0] = self._work[0] + 1

    ############################################################
    # All prime numbers are appended to the list.
    # Nothing can be changed
    ###########################################################
    def _append_prime_number(self, p):
        self._prime_number_list.append(p)

    ##Required function to implement
    def up_to_primes(self) -> "None":
        ## NOTHING CAN BE CHANGED HERE
        ## you cannot call log from Python library
        self._up_to_primes()

    ##Required function to implement
    def sieve_of_eratosthenes(self) -> "None":
        ## NOTHING CAN BE CHANGED HERE
        ## YOU CANNOT CALL math.log from Python library
        self._sieve_of_eratosthenes()

    ############################################################
    # Implement your code BELOW
    # You can have any number of private variables and functions
    # YOU CANNOT CALL math.log from Python library
    ###########################################################
    
    # If a num can't be divided by any prime number, it's a prime number
    def _up_to_primes(self):
        # if self._n < 2:
        #     return 0

        # We know 2 is the first prime number
        self._prime_number_list.append(2)

        for num in range(3, self._n, 2): # don't need to check even numbers
            if self._isPrime(num):
                self._append_prime_number(num)
                print(self._prime_number_list)

                self._increment_work_done()

    def _isPrime(self, n):
        for primer in self._prime_number_list:
            if primer ** 2 > n:
                break
            if n % primer == 0:
                return False
        return True

    # Most efficient solution
    def _sieve_of_eratosthenes(self):
        sieve = [True] * self._n
        sieve[0] = False
        sieve[1] = False

        # private method to get square root of n
        root = self._get_root(self._n)

        for i in range(2, root + 1):
            if sieve[i] is True:

                factor = 2
                while factor * i < self._n:
                    sieve[factor * i] = False
                    factor += 1

                    self._increment_work_done() # To be verified...
        
        for i, n in enumerate(sieve):
            if n is True:
                self._prime_number_list.append(i)

    # Binary search to get square root. O(logN)
    def _get_root(self, n):
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 <= n and (mid + 1) ** 2 > n:
                return mid
            elif mid ** 2 < n:
                left = mid
            else:
                right = mid

            self._increment_work_done()
            
solution = Solution()
print(solution.countPrimes(100))