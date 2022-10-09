# coding=utf-8
# Author:Duome
"""

1、思路：
    每个月的兔子分为k1第一个月兔子（萌新），k2第二个月的兔子（不可生育），k3第三个月及以上（可生育）
    从第三个月开始：
        可生育的兔子，是上个月可生育的兔子加上上个月不可生育的兔子数
        不可生育的兔子数，是上个月萌新的兔子数
        萌新的兔子数，是这个月可生育的兔子数
    第一个月：
        可生育的兔子数是0
        不可生育的兔子数是0
        萌新是1
    第二个月
        可生育的兔子数是0
        不可生育的兔子书是1
        萌新是0
"""
try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        m = int(line)
        k3 = 0
        k2 = 0
        k1 = 1
        for i in range(m):
            k3 += k2
            k2 = k1
            if i == 1:
                k1 = 0
            else:
                k1 = k3
        print k3 + k2 + k1
except:
    pass

"""

1、思路：
    递归
    每次的模式都是一样的，上一个数加上上上一个数
    斐波那契数列：1 1 2 3 5 8 13 21 34 f(n)=f(n-1)+f(n-2) n>2,n从0开始
    或者斐波那契数列：1 1 2 3 5 8 13 21 34 f(n)=f(n-1)+f(n-2) n>3,n从1开始
    
    
"""
def func(n):
    if n < 3:
        return 1
    return func(n-1) + func(n-2)

try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        res = func(int(line))
        print res
except:
    pass