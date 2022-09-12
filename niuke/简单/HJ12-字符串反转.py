# coding=utf-8
# Author:Duome
"""

1、思路：
    利用列表反转功能

"""
try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        res = ''.join(list(line)[::-1])
        print res

except:
    pass
