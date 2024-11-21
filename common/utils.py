# -*- coding: utf-8 -*-
# @Time    : 2024/11/26
# @Author  : kyra.hu
# @File    : utils.py
# @Software: PyCharm


import yaml
from jsonpath import jsonpath
from loguru import logger
from string import Template
from faker import Faker
from common.wraaper import assert_log
from conf.config import Data



class Utils:
    """提供工具方法"""


    @classmethod
    def handle_yaml(cls, file_path:str):
        """
        读取yaml文件
        :param file_name:
        :return:
        """
        try:
            yaml_data = yaml.safe_load(open(file_path, encoding='utf-8'))
        except Exception as e:
            logger.error(f'yaml文件读取失败，文件名称：{file_path}')
            raise e
        else:
            return yaml_data


    @classmethod
    def template(cls, source_data:dict, replace_data: dict):
        """
        替换文本变量
        :param source_data:   {phone_: $phone_}
        :param replace_data:  {phone_: 'new_phone'}
        :return:
        """
        res = Template(str(source_data)).safe_substitute(**replace_data)
        return yaml.safe_load(res)


    @classmethod
    def handle_random_phone(cls):
        """
        生成随机手机号
        :return:
        """
        fake = Faker(locale='zh_CN')
        phone_number = fake.phone_number()
        return phone_number


    @classmethod
    def extract(cls,resp:dict,expr=None):
        """
        提取响应结果
        :param resp: json
        :param expr: {"token":"$..token"}
        :return:
        """
        if expr == None:
            logger.info('提取表达式为空！')
        else:
            for key, value in expr.items():
                actual = jsonpath(resp, value)[0]
                if actual:
                    setattr(Data, key, str(actual))
                    logger.info(f'提取{key}成功')
                else:
                    logger.warning('没有提取到数据')


    @classmethod
    @assert_log
    def assert_resp(cls,resp: dict, expr: dict):
        """
        断言相等
        :param resp: json
        :param assert_expr: 提取表达式:预期结果  {"$..status":1,"$..msg":"登录成功"}
        :return: True或者False
        """
        if resp and expr:
            for key, value in expr.items():
                actual = jsonpath(resp, key)[0]
                try:
                    assert actual == value
                except:
                    return False
            return True
        else:
            return False