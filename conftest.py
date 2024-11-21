# -*- coding: utf-8 -*-
# @Time    : 2024/11/26
# @Author  : kyra.hu
# @File    : conftest.py
# @Software: PyCharm


import pytest,warnings
from loguru import logger

2
#class级别fixture
@pytest.fixture(scope='class')
def setup_teardown_class():
    warnings.filterwarnings("ignore")
    logger.info(f'-----------------开始执行用例----------------')
    yield
    logger.info(f'-----------------用例执行结束----------------')