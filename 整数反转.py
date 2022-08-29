# coding=utf-8
# author:Duome
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        整数反转：
        1、思路：将数字的最后一个位取出来，推入一个结果中，当无法取出最后一位数的时候返回结果
        2、保证反转后的数没有超过64位
        3、取数的时候如果是负数，且余数不为0的时候需要特殊处理
        4、取出最后以为数后的数字，因为有负数的存在需要特殊处理
        """
        rev = 0
        while True:
            # 当x的末尾数都处理完成之后，就返回rev
            if x == 0:
                return rev
            # 这里需要每次判断每次反转后是否超出64位
            if rev < -2**31/10 + 1 or rev > 2**31/10:
                return 0
            # 取出x末尾的数字
            d = x % 10
            # 如果是负数，余数为正数或者0，当余数为整数的时候需要处理
            if x < 0 and d != 0:
                d = d - 10
            # 如果是负数，商可能为整数，所以把个位删除在做除
            x = (x - d) // 10
            rev = rev * 10 + d

if __name__ == '__main__':
    S = Solution()
    r = S.reverse(-10)
    print r
