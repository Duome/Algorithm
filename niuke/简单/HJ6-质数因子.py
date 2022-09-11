# coding=utf-8
# Author:Duome
"""

1、思路：
    质数是大于一且除了1和本身没有约数的数，最小的质数是2
    如果一个数字是合数，则从2开始循环除质数，除到不能除后增加除数；
        （如果 x是质数，那么大于 x的 x的倍数 2x,3x,… 一定不是质数;）
    如果一个数字是合数，那么它最小的质因子不会超过它的平方根。
    对于一个质数 x，如果按上文说的我们从 2x 开始标记其实是冗余的，应该直接从x⋅x开始标记，因为2x,3x,… 这些数一定在xx之前就被其他数的倍数标记过了

"""

try:
    while True:
        line = int(raw_input().strip())
        if not line:
            break
        # 最小的质数是2
        i = 2
        line_list = []
        # 如果一个数是合数才需要循环找其中的质数
        # 如果一个数字是合数，那么它最小的质因子不会超过它的平方根。
        while i <= line ** 0.5:
            # 从最小的数开始除，如果除不尽了，在加1，每个数num
            if line % i == 0:
                line_list.append(i)
                line = line / i
            else:
                i += 1
        # 此时的line必然是一个质数
        line_list.append(line)
        res = ' '.join(map(lambda x: str(x), line_list))
        print res

except:
    pass



