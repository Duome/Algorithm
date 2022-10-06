# coding=utf-8
# Author:Duome
"""

1、思路：
        利用集合的特点获取字符串中的元素
        利用字符串count和列表sorted找到最少的字符个数
        遍历列表，用列表remove方法把列表中的字符删除

"""
try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        lines = list(line)
        line_list = list(set(list(line)))
        num = sorted(map(lambda x: line.count(x), line_list))[0]
        for i in line_list:
            if line.count(i) == num:
                for j in xrange(num):
                    lines.remove(i)

        print ''.join(lines)
except:
    pass
