# coding=utf-8
# Author:Duome
"""
1、思路：从右向左——使用列表反转；
        不含重复数字且保持顺序——生成新劣币哦，遍历原列表不重复的加入新列表
        列表转换为字符串
"""
try:
    while True:
        line = raw_input().strip()
        if line == '':
            break
        line_res = list(line)[::-1]
        num = []
        for i in line_res:
            if i not in num:
                num.append(i)
        rev = ''.join(num)
        print rev
except:
    pass
