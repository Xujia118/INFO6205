class Solution:
    def __init__(self) -> None:
        pass

    def alg(self, coins, removed_coin=None):
        n = len(coins)

        # base case 1
        if n == 2:
            # we know the fake is not in this group
            # we have to look in the other group
            if coins[0] == coins[1]:
                fake = removed_coin
                return
            else:
                if coins[0] != removed_coin:
                    fake = coins[0]
                else:
                    fake = coins[1]
                return

        if n == 3:
            if coins[0] == coins[1]:
                fake = coins[2]
                return self.verdict(fake, coins[0])
            # otherwise, we know the fake is left or right, the removed coin is real
            else:
                if coins[2] == coins[0]:
                    fake = coins[1]
                    return self.verdict(fake, coins[0])
                else:
                    fake = coins[0]
                    return self.verdict(fake, coins[1])

        # base case 2
        if n == 4:
            if coins[0] == coins[1]:
                # we know the fake is in the coins2 and 3
                if coins[2] != coins[0]:
                    fake = coins[2]
                else:
                    fake = coins[3]
                return self.verdict(fake, coins[0])
            else:
                # we know the fake is in coins0 and 1
                if coins[0] != coins[2]:
                    fake = coins[0]
                else:
                    fake = coins[1]
                return self.verdict(fake, coins[2])

        if n % 2 == 0:
            mid = n // 2
        else:
            mid = (n - 1) // 2
            removed_coin = coins.pop()

        left_sub = coins[:mid]
        right_sub = coins[mid:]

        compare_result = self.compare(left_sub, right_sub)
        if compare_result == '=':
            fake = removed_coin
            real = left_sub[0]
            return self.verdict(fake, real)
        elif compare_result == '<':
            return self.alg(left_sub, removed_coin)
        else:
            return self.alg(right_sub, removed_coin)

    def compare(self, left, right):
        left_sum = sum(left)
        right_sum = sum(right)

        if left_sum == right_sum:
            return '='
        elif left_sum > right_sum:
            return '>'
        else:
            return '<'

    # def finalCompare(self, arr):

    def verdict(self, fake, real):
        if fake < real:
            return True
        else:
            return False


coins = [1, 2, 2, 2, 2]
solution = Solution()
print(solution.alg(coins))
