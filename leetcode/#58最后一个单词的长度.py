# coding=utf-8
# author:Duome
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])


if __name__ == '__main__':
    S = Solution()
