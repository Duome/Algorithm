# coding=utf-8
# Author:Duome
"""

1、思路：
    利用sort排序

"""
try:
    while True:
        num = int(raw_input().strip())
        if not num:
            break
        line_list = []
        for i in xrange(num):
            line = raw_input().strip()
            if not line_list:
                line_list.append(line)
            else:
                if line >= line_list[-1]:
                    line_list.append(line)
                else:
                    for j in line_list:
                        if line <= j:
                            line_list.insert(line_list.index(j), line)
                            break

        for res in line_list:
            print res

except:
    pass

try:
    while True:
        num = int(raw_input().strip())
        if not num:
            break
        line_list = []
        for i in xrange(num):
            line = raw_input().strip()
            line_list.append(line)
        line_list.sort()
        for res in line_list:
            print res


except:
    pass