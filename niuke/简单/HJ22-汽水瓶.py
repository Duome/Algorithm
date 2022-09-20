# coding=utf-8
# Author:Duome
"""

1、思路：
    递归
    每次的模式都是一样的，拿空瓶子，换汽水
    当瓶子数小于3时，无法递归：
        空瓶子数为0或者1的时候，直接return结果
        空瓶子数为为2的时候，结果需要加1
"""
def change_bottle(n):
    get_bottel = n // 3
    remain_bottle = get_bottel + n % 3
    res = get_bottel
    if n < 3:
        if n <= 1:
            res = res
        elif n < 3:
            res += 1
    else:
        res += change_bottle(remain_bottle)
    return res
try:
    while True:
        line = int(raw_input().strip())
        if not line:
            break
        res = change_bottle(line)
        print res
except:
    pass
