# coding=utf-8
# author:Duome
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i > target:
                    return nums.index(i)
        return len(nums)


if __name__ == '__main__':
    S = Solution()
