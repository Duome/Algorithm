# coding=utf-8
# author:Duome
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif ''.join(list(str(x))[::-1]) == str(x):
            return True
        else:
            return False



if __name__ == '__main__':
    S = Solution()
