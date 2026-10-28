class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lef = 1
        rig = len(numbers)

        while lef<=rig:
            sum = numbers[lef-1] + numbers[rig-1]
            if sum > target:
                rig -= 1
            elif sum < target:
                lef += 1
            else:
                return [lef,rig]
        return []