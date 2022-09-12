# coding=utf-8
# Author:Duome
"""

1、思路：
    利用集合的，元素不重复的特征
    集合有len属性

"""
try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        res = len(set(list(line)))
        print res

except:
    pass
