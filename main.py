# -*- coding: utf-8 -*-
# @Time    : 2024/11/26
# @Author  : kyra.hu
# @File    : main.py.py
# @Software: PyCharm


import pytest,os
from loguru import logger
from common.handle_path import log_full_path,allure_files,allure_report



logger.add(log_full_path, level='INFO', backtrace=True, diagnose=True, encoding='utf-8')
pytest.main(['-v','--alluredir=outputs/allure_files',
             "--clean-alluredir", '-s', '-W',
             'ignore:Module already imported:pytest.PytestWarning'])
os.system(f'allure generate {allure_files} -o {allure_report} -c')