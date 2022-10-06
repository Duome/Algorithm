# coding=utf-8
# Author:Duome
"""

1、思路：
    使用sorted方法来以ASCII码值排序

"""
try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        res = ''.join(sorted(line))
        print res
except:
    pass
