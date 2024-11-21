# -*- coding: utf-8 -*-
# @Time    : 2024/11/26
# @Author  : kyra.hu
# @File    : handle_path.py
# @Software: PyCharm


import os
import datetime


#项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置文件目录
CONF_DIR = os.path.join(BASE_DIR,'conf')

#case文件目录
CASE_DIR = os.path.join(BASE_DIR,'data')

#日志格式+路径
log_filename = '{}_{}.log'.format('test',datetime.datetime.now().strftime('%Y_%m_%d_%H:%M:%S'))
log_full_path = os.path.join(os.path.join(BASE_DIR,'outputs','log'),log_filename)

#allure_files
allure_files = os.path.join(BASE_DIR,'output','allure_files')

#allure_report
allure_report = os.path.join(BASE_DIR,'output','report')
