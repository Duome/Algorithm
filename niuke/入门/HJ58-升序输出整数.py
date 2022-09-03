# coding=utf-8
# Author:Duome
"""
1、思路：
    获取输入的第一个信息，第一个输入的第二个元素——多少个整数；
    获取输入的第二个信息，整数数组
    升序需要转化为数字之后排序
    数字需要转化为字符串之后在合并（join的时候列表中的元素需要是字符串类型）
"""
try:
    while True:
        line = raw_input().strip()
        line_leng = int(line.split(' ')[-1])
        line_num = map(lambda x: int(x), raw_input().strip().split(' '))
        if not line:
            break
        res = ' '.join(map(lambda x: str(x), sorted(line_num)[:line_leng]))
        print res
except:
    pass
