# coding=utf-8
# Author:Duome
"""
1、思路：
    获取输入的第一个信息，输入里的最后元素
    使用len方法获取长度
"""
try:
    while True:
        line = raw_input().strip()
        line_end = line.split(' ')[-1]
        if not line:
            break
        print len(line_end)
except:
    pass
