class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lef = 0 
        rig = len(numbers) - 1

        while lef < rig:
            sum = numbers[lef] + numbers[rig]
            if sum < target:
                lef += 1
            elif sum > target:
                rig -= 1
            else:
                return[lef+1,rig+1]
                