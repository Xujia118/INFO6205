import math

class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes
        # Initialize an aray
        sieve = [True] * n
        
        # We know 0 and 1 are not sieve
        sieve[0] = False
        sieve[1] = False

        root = int(math.sqrt(n))
        # begin with the first index marked True, 2
        for i in range(2, root + 1):
            if sieve[i] is True:

                # times a factor: all the product is not a primer
                factor = 2
                while factor * i < n:
                    sieve[factor * i] = False
                    factor += 1
        
        return [i for i, n in enumerate(sieve) if n is True]
        # return sum(sieve)

        # prime_number_list = [2]

        # for num in range(3, n):
        #     for primer in prime_number_list:
        #         if num % primer == 0:
        #             break
        #     else:
        #         prime_number_list.append(num)
                    
        # return prime_number_list

        # Approach 1: Old way
        # count = 0
        # result = []
        
        # for num in range(2, n):
        #     root = int(math.sqrt(num))
        #     for i in range(2, root + 1):
        #         if num % i == 0:
        #             break
        #     else:
        #         result.append(num)
        #         # count += 1
        
        # # return count
        # return result
            
n = 10
solution = Solution()
print(solution.countPrimes(n))