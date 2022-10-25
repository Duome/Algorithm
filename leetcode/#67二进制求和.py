# coding=utf-8
# author:Duome
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]


if __name__ == '__main__':
    S = Solution()
