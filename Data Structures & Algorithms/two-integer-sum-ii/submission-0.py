class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen_set=set()
        for i in range(len(numbers)):
            if (target-numbers[i]) in seen_set:
                j = numbers.index(target - numbers[i])
                return [j + 1, i + 1]
            else:
                seen_set.add(numbers[i])
        