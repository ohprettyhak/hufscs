"""
Created on: 06/09/2024

Program: Large Memory List
Author: Hak Lee
"""

_list = []

elements = 100 ** 9  # 1 billion elements

for i in range(elements):
    _list.append(i)

print('list count:', len(_list))
input('enter to exit')
