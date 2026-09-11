class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums=sorted(nums)
        count=1
        longest=1
        for i in range(1,len(sorted_nums)):
            current=sorted_nums[i]
            previous=sorted_nums[i-1]

            if current==previous:
                continue
            elif current==previous+1:
                count+=1
            else:
                count=1
            
            longest=max(longest,count)
        return longest




        