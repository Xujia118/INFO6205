class PermutateArray:
    def __init__(self) -> None:
        pass

    def useRecursion(self, arr):
        if len(arr) == 1:
            return [arr]

        result = []
        for idx, char in enumerate(arr):
            for perm in self.useRecursion(arr[:idx] + arr[idx + 1:]):
                result.append([char] + perm)
        return result

    def useStructy(self, i=0):
        if i > len(self.arr) - 1:
            return [[]]

        first = self.arr[i]
        result = []

        for perm in self.useStructy(i + 1):
            for j in range(len(perm) + 1):
                result.append(perm[:j] + [first] + perm[j:])

        return result


arr = ['a', 'b', 'c']
permutateArray = PermutateArray()
print(permutateArray.useRecursion(arr))


class PermutateString:

    def __init__(self, s) -> None:
        pass

    def useRecursion(self, s):
        if len(s) == 1:
            return [s]

        result = []
        for i, c in enumerate(s):
            for perm in self.useRecursion(s[:i] + s[i + 1:]):
                result.append(c + perm)
        return result

    # def useStructy(self, i=0):
    #     if i > len(self.s) - 1:
    #         return []

    #     first = self.s[i]
    #     result = ""

    #     for perm in self.useStructy(i + 1):
    #         for j in range(len(perm) + 1):
    #             result.append()


# s = '123'
# permutateString = PermutateString(s)
# print(permutateString.useRecursion(s))
