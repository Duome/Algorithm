# coding=utf-8
# Author:Duome
"""

1、思路：
        使用97-123的字符小写来排除非字母的元素
        将不是字母的元素全部转化为空格
        使用字符串replace方法替换非字母的元素
        使用字符串split方法获取所有单词
        使用列表反转方法进行反转
        使用字符串join方法把反转的单词重新拼凑


"""
try:
    while True:
        line = raw_input().strip()
        chr_list = [chr(i) for i in range(97, 123)]
        if not line:
            break
        line_len = len(line)
        for i in xrange(line_len):
            if line[i].lower() not in chr_list:
                line = line.replace(line[i], ' ')
        res = ' '.join(line.split()[::-1])
        print res
except:
    pass
