class Solution:
    def __init__(self) -> None:
        pass

    def alg(self, coins):
        n = len(coins)

        # base case 1
        if n == 1:
            # Since there's only one coin left, it must be the fake one.
            return coins[0]

        # base case 2
        if n == 2:
            # We have only two coins left, we compare them directly.
            return coins[0] if coins[0] < coins[1] else coins[1]

        # Split the coins into two groups
        if n % 2 == 0:
            mid = n // 2
            left_sub = coins[:mid]
            right_sub = coins[mid:]
        else:
            mid = (n - 1) // 2
            left_sub = coins[:mid]
            right_sub = coins[mid + 1:]
            removed_coin = coins[mid]

        # Compare the two groups
        compare_result = self.compare(left_sub, right_sub)
        if compare_result == '=':
            # Recur on the removed coin and the remaining coins
            return self.alg([removed_coin])
        elif compare_result == '<':
            # Recur on the left subgroup
            return self.alg(left_sub)
        else:
            # Recur on the right subgroup
            return self.alg(right_sub)

    def compare(self, left, right):
        left_sum = sum(left)
        right_sum = sum(right)

        if left_sum == right_sum:
            return '='
        elif left_sum > right_sum:
            return '>'
        else:
            return '<'

    def verdict(self, fake, real):
        if fake < real:
            return 'Light'
        else:
            return 'Heavy'


coins = [4, 2, 2, 2, 2, 2, 2]
solution = Solution()
print(solution.alg(coins))
