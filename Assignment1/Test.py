import random
from Algorithm import Solution

class Test:
    def __init__(self):
        self.solution = Solution()

    def _simpleTest(self):
        cases = [
            [-4,-1,0,3,10],
            [-7,-3,2,3,11],
            [-11,-5,0,1,3]
        ]

        for case in cases:
            expected = self._get_correct_answer(case)
            answer = self.solution.sortedSquares(case)
            
            print("Expected:", expected)
            print("output:", answer)
            
            if answer == expected:
                print("Correct!")
            else:
                print("Incorrect!")
            
    def _randomTest(self):
        randomList = self._generateRandomList()
        
        for case in randomList:
            excepted = self._get_correct_answer(case)
            answer = self.solution.sortedSquares(case)

            if answer != excepted:
                print("Incorrect")
                return (excepted, answer)
        
        return "Good job!"
    
    def _get_correct_answer(self, case: list[int]):
        case = [n ** 2 for n in case]
        return sorted(case)
    
    @staticmethod
    def _generateRandomList():
        randomList = [] # List[List[int]]

        for i in range(random.randint(0, 100)):
            oneList = [random.randint(-100, 100) for _ in range(random.randint(0, 100))]
            randomList.append(sorted(oneList))

        return randomList

mytest = Test()
print(mytest._simpleTest())
print(mytest._randomTest())
