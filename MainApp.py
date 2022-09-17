#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:10:26 2022

@author: zhouguangdi
"""


# 从PyQt5中导入PyQt控件
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
# 导入pyqtSlot来连接滑块和DoubleSpinBox信号
from PyQt5.QtCore import pyqtSlot
# 从uic模块生成的UiMainApp.py中导入Ui_MainWindow类
from UiMainApp import Ui_MainWindow

from openpyxl import load_workbook

from gtts import gTTS

from playsound import playsound

import os

class MainApp(QMainWindow, Ui_MainWindow):
    """
    MainApp继承QMainWindow以及UiMainApp模块中的Ui_MainWindow
    """
    def __init__(self):
        """构造函数或初始化程序"""
        QMainWindow.__init__(self)
        # 必须调用 self.setuoUi(self) 来初始化界面
        self.setupUi(self) # 这是被自动地定义在design.py文件中的，它设置被定义的布局和控件
        
    def getInfo(self):
        file = QFileDialog()
        if file.exec_():
            filename=file.selectedFiles()[0]
            self.lineEdit_location.setText(filename)
            self.textBrowser_location.setPlainText("导入单词库成功！单词库地址为："+filename)
            global location
            location = filename
            
    def read_xlsx(self):
        wb = load_workbook(location)
        sheets = wb.worksheets
        sheet1 = sheets[0]
        
        global col1, col2, col3
        
        col1 = []
        for col01 in sheet1['A']:
            col1.append(col01.value)
        
        col2 = []
        for col02 in sheet1['B']:
            col2.append(col02.value)
            
        col3 = []
        for col03 in sheet1['C']:
            col3.append(col03.value)
    
    def get_word_mp3(self):
        L = []
        for root, dirs, files in os.walk('./'):   # 获取已经下载的单词发音列表
            for file in files:
                if os.path.splitext(file)[1]  == '.mp3':
                    L.append(os.path.splitext(file)[0])
                                       
        number_of_words = len(col1)
        for n in range(number_of_words):
            if n == 0:
                continue
            else:
                #for word_n in range(len(L)):
                if col1[n] in L:
                    continue
                else:
                    tts = gTTS(col1[n], lang='en', tld='cn')
                    tts.save(col1[n]+'.mp3')
   
    def first_word(self):
        global sequence
        sequence = 0

    def display_word(self):
        self.textBrowser_word.setHtml("<font size=6>"+col1[sequence]+"</font>")
        self.textBrowser_phonetics.setHtml("<font size=6>"+col3[sequence]+"</font>") #音标放到第三个框内
        self.textBrowser_Paraphrase.setHtml("<font size=6>"+col2[sequence]+"</font>")
    
    def play_word_mp3(self):
        if sequence == 0:
            print("开始背单词吧！") 
        else:
            playsound(col1[sequence]+'.mp3')   
        
    #点击按钮的槽
    @pyqtSlot()
    def on_pushButton_location_clicked(self):  # 读取词库
        self.getInfo()   
        self.read_xlsx()
        self.first_word()
        self.display_word()
        self.get_word_mp3()
        #self.play_word_mp3()
      
    @pyqtSlot()
    def on_pushButton_next_clicked(self):  # 下一个单词  
        global sequence
        if sequence < len(col1)-1:
            sequence = sequence + 1
        else:
            sequence = 0
        self.display_word()
        #self.play_word_mp3()
            
    @pyqtSlot()
    def on_pushButton_player_clicked(self):  # 下一个单词  
        self.play_word_mp3()
    
    

        
    @pyqtSlot()
    def on_pushButton_Previous_clicked(self):  # 上一个单词  
        global sequence
        if sequence + len(col1)-1>=0: 
            sequence = sequence - 1
        else:
            sequence =-1
        self.display_word()
        #self.play_word_mp3()
        
    @pyqtSlot()
    def on_pushButton_goback_clicked(self):  # 回到第一个单词  
        self.first_word()
        self.display_word()
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainApp()
    MyApplication.show() # Show the form
    sys.exit(app.exec_())  # 执行应用程序