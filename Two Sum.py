class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lis = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == int(target):
                    lis.append(i)
                    lis.append(j)
                    break
        return lis

                    
        

#======================TEST======================#
# target = 9
# nums = [2,7,11,15]
# target = 9
# nums = nums.replace('[', '')
# nums = nums.replace(']', '')
# s = Solution()
# s.twoSum(nums,target)
#===============================================#

