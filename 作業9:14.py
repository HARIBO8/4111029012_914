#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:27:43 2023

@author: keigo
"""

def memory_addressing(page_table, page_size,logical_address):
# 計算頁號和偏移量
    page_number, offset = divmod(logical_address, page_size)
    
    # 查找頁表來獲得相應的框架號
    if page_number in page_table:
        frame_number = page_table[page_number]
        # 計算物理地址
        physical_address = frame_number * page_size + offset
        print(f"The physical address is {physical_address}")
    else:
        print("Invalid page number, address translation failed.")
# 定義頁表，其中鍵是頁號，值是框架號
print('請你輸入三次框架號')
a = int(input('請你輸入第一頁的框架號:'))
b = int(input('請你輸入第二頁的框架號:'))
c = int(input('請你輸入第三頁的框架號:'))


page_table = {0: a, 1: b, 2: c}
# 定義頁大小（例如：4096字節）
page_size = 4096
# 定義邏輯地址（例如：7000）
logical_address = int(input("請你輸入邏輯地址："))
# 調用函數進行地址轉換
memory_addressing(page_table, page_size, logical_address)