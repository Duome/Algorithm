# coding=utf-8
# author:Duome
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in xrange(l-1):
            for j in xrange(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    S = Solution()
