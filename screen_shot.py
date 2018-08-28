#!/bin/env python
#-*- coding:utf-8 -*-
import subprocess
class Screenshot():#截取手机屏幕并保存到电脑
    def __init__(self):
        #查看连接的手机
        connect=subprocess.Popen("adb devices",stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        stdout,stderr=connect.communicate()   #获取返回命令
        #输出执行命令结果结果
        if stdout:
            stdout=stdout.decode("utf-8")
        else:
            raise RuntimeError(stderr.decode("gbk"))
 
    def screen(self,cmd):#在手机上截图
        screenExecute=subprocess.Popen(str(cmd),stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        stdout, stderr = screenExecute.communicate()
        # 输出执行命令结果结果
        if stderr:
            raise RuntimeError(stderr.decode("gbk"))

 
    def saveComputer(self,cmd):#将截图保存到电脑
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        if stdout:
            print('picture save')
 
    def getScreen(self, path):
        cmd_crn_shot=r"adb shell /system/bin/screencap -p /sdcard/screen.png"       #命令1：在手机上截图3.png为图片名
        cmd_pull_picture=r"adb pull /sdcard/screen.png " + path                       #命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
        self.screen(cmd_crn_shot)
        self.saveComputer(cmd_pull_picture)
