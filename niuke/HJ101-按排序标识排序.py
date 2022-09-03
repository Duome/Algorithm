# coding=utf-8
# Author:Duome
"""
1、思路：
    获取输入的第一个信息，元素个数，没有需要判断的地方获取就可以了；
    获取输入的第二个信息，整数数组
    获取输入的第三个信息，排序标识
    升序需要转化为数字之后排序
    数字需要转化为字符串之后在合并（join的时候列表中的元素需要是字符串类型）
"""
try:
    while True:
        line_leng = raw_input().strip()
        line_nums = map(lambda x: int(x), raw_input().strip().split(' '))
        line_tag = raw_input().strip()
        if not line_leng:
            break
        if line_tag == '0':
            res = ' '.join(map(lambda x: str(x), sorted(line_nums)))
        else:
            res = ' '.join(map(lambda x: str(x), sorted(line_nums)[::-1]))
        print res
except:
    pass
