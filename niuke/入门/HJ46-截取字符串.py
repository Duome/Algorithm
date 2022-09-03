# coding=utf-8
# Author:Duome
"""
1、思路：
    获取两个输入（注意输入的都是字符串，如果需要数字需要改变数据类型int（））
    使用列表的截取特性获取对应的元素
    将字符串转为列表后又转为字符串
"""
try:
    while True:
        line_str = raw_input().strip()
        line_num = int(raw_input().strip())
        if not line_str:
            break
        rev = ''.join(list(line_str)[:line_num])
        print rev
except:
    pass
