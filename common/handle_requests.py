# -*- coding: utf-8 -*-
# @Time    : 2024/11/26
# @Author  : kyra.hu
# @File    : handle_requests.py
# @Software: PyCharm


import requests
from conf.config import dev,headers
from common.wraaper import api_log,singleton
from conf.config import Data


@singleton
class HandleRequest:
    """
    请求处理
    """

    def __init__(self):
        self.s = requests.Session()
        self.s.headers = headers
        self.base_url = dev


    @api_log
    def send_request(self,method,url,data=None,**kwargs):
        """
        :return: json字符串
        """

        self.__header()
        url = self.__url(url)
        if method.upper() == "GET":
            resp = self.s.get(url=url, params=data,verify=False,**kwargs)
        else:
            resp = self.s.request(method=method, url=url, data=data,verify=False, **kwargs)
        return resp


    def __header(self):
        """
        :param token: token处理
        :return:
        """
        if hasattr(Data,'token'):
            self.s.headers.update({'token':getattr(Data,'token')})


    def __url(self,url):
        """
        :param url:URl处理 请求不同地址时写上完整路径
        :return:
        """
        if url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            return self.base_url + url