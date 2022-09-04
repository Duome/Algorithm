# coding=utf-8
# Author:Duome
"""
1、思路：
    计算输入的长度是否大于8，如果小于8的话，需要吧小于的长度替换成0加在字符串后面再打印；
    如果长度大于8，循环分隔打印长度8的字符，最后一个循环判断：
        如果是8，直接打印；
        如果是0，不打印；
        如果小于8，小于的长度替换成0后加载字符串后打印
"""
try:
    while True:
        line = raw_input().strip()
        num = 8
        if not line:
            break
        line_times = len(line) // num
        if line_times == 0:
            zero_times = 8 - len(line)
            print line + '0' * zero_times
        else:
            tag = 0
            for i in xrange(line_times + 1):
                if i != line_times:
                    print line[tag: tag + 8]
                else:
                    line_end = line[tag:]
                    if len(line_end) == 8:
                        print line[tag: tag + 8]
                    elif len(line_end) == 0:
                        break
                    else:
                        zero_times = 8 - len(line_end)
                        print line_end + '0' * zero_times
                tag += 8
except:
    pass
