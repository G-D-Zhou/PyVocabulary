#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:03:25 2022

"""

'''PyQt5 uic 模块将ui文件(XML代码)转化为py文件(Python代码) '''
from PyQt5 import uic
fin = open('UiMainApp.ui', 'r')
fout = open('UiMainApp.py', 'w')
uic.compileUi(fin,fout,execute=True)
fin.close()
fout.close()
