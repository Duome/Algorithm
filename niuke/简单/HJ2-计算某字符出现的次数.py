# coding=utf-8
# Author:Duome
"""
1、思路：
    将输入一传化为全小写；
    将输入二转化为全小写；
    使用字符串的count属性
"""
try:
    while True:
        line = raw_input().strip().lower()
        line_tag = raw_input().strip().lower()
        res = line.count(line_tag)
        if not line:
            break
        print res
except:
    pass
