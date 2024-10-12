class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        compliment = None
        n = len(numbers)
        end = n - 1
        for start in range(n - 1):
            compliment = target - numbers[start]
            while end > start:
                if numbers[end] == compliment:
                    res.append(start + 1)
                    res.append(end+ 1)
                    return res
                if numbers[end] < compliment:
                    break
                end -= 1
        return None
                
