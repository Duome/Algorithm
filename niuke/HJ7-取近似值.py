# coding=utf-8
# Author:Duome
"""
1、思路：数字取整数部分后，减去整数部分，得到的数小于0.5取整数部分，否则取整数部分+1
"""
try:
    while True:
        line = raw_input().strip()
        if line == '':
            break
        i = float(line)
        i_int = int(i)
        if i - i_int < 0.5:
            rev = i_int
        else:
            rev = i_int + 1
        print rev
except:
    pass