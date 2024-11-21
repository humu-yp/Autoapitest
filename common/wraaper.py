# -*- coding: utf-8 -*-
# @Time    : 2024/11/26
# @Author  : kyra.hu
# @File    : wraaper.py
# @Software: PyCharm


from jsonpath import jsonpath
from loguru import logger
import urllib3
from functools import wraps

urllib3.disable_warnings()



def api_log(func):
    """
    接口请求记录
    :param func:
    :return: response
    """
    @wraps(func)
    def inner(*args,**kwargs):
        logger.info(f'请求接口：{kwargs["url"]}')
        logger.info(f'请求方式：{kwargs["method"]}')
        logger.info(f'请求参数：{kwargs["data"]}')
        res = func(*args,**kwargs)
        try:
            logger.info(f'响应body：\n{res.json()}')
            logger.info(f'响应status：{res.status_code}')
        except:
            logger.warning('响应body不是json类型!')
            logger.info(f'响应body：\n{res.text}')
        return res
    return inner


def assert_log(func):
    """
    断言日志记录
    :param func:
    :return: response
    """
    @wraps(func)
    def inner(*args,**kwargs):
        logger.info(f'jsonpath表达式：{[key for key,value in args[2].items()]}')
        logger.info(f'预期结果: {[value for key,value in args[2].items()]}')
        logger.info(f'实际结果: {[jsonpath(args[1], key)[0] for key, value in args[2].items()]}')
        res = func(*args,**kwargs)
        if res == True:
            logger.info('断言结果: 成功')
        else:
            logger.exception('断言结果: 失败!')
        return res
    return inner


def singleton(cls):
    # 单例模式 创建一个字典来存储类和对象的映射关系
    dic = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if dic.get(cls):
            return dic[cls]
        else:
            dic[cls] = cls(*args, **kwargs)
            return dic[cls]
    return wrapper