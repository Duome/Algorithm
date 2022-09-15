# coding=utf-8
# Author:Duome
"""

1、思路：
    获取字母列表，供大写的字符转码；
    生成小写字母转码的字典；
    字母大写判断isupper，字母小写判断islower，都为false就是数字；
    大写字母转码需要注意，字母z转为a

"""
try:
    while True:
        line = raw_input().strip()
        if not line:
            break
        str_list = [chr(i) for i in range(97, 123)]
        str_dict = {'abc': '2',
                    'def': '3',
                    'ghi': '4',
                    'jkl': '5',
                    'mno': '6',
                    'pqrs': '7',
                    'tuv': '8',
                    'wxyz': '9'
                    }
        res_list = []
        str_dict_keys = str_dict.keys()
        for i in line:
            if i.islower():
                for j in str_dict_keys:
                    if i in j:
                        res_list.append(str_dict[j])
                        break
            elif i.isupper():
                if i == 'Z':
                    res_list.append('a')
                else:
                    res_list.append(str_list[str_list.index(i.lower()) + 1])
            else:
                res_list.append(i)
        print ''.join(res_list)
except:
    pass
