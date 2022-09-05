# coding=utf-8
# Author:Duome
"""

1、思路：
    进制准换十转十六hex、十转二bin、其他转十int

"""
try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        res = int(line, 16)
        print res
except:
    pass
