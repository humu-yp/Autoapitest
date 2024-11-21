# -*- coding: utf-8 -*-
# @Time    : 2024/11/26
# @Author  : kyra.hu
# @File    : handle_mysql.py
# @Software: PyCharm


import pymysql
from loguru import logger
from conf.config import mysql
from wraaper import singleton

@singleton
class HandleMysql:
    """
    提供数据库方法
    """
    try:
        def __init__(self):
            """
            由配置文件读取
            """
            self.conn = pymysql.connect(
                host=mysql['host'],
                port=mysql['port'],
                user=mysql['user'],
                password=mysql['password'],
                database=mysql['database'],
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor,
            )
            logger.info(f'数据库连接信息: {mysql}')
            self.cur = self.conn.cursor()
    except:
        logger.exception('数据库连接失败！！！')
        raise


    def get_count(self,sql):
        """
        获取sql执行后的结果条数
        :param sql:
        :return:
        """
        count = self.cur.execute(sql)
        logger.info(f'执行sql: {sql}，获取结果条数为{count}')
        return count


    def update(self,sql:str):
        """
        执行更新sql，多条就往list内加字典
        :param sql: '[{"sql": "UPDATE boc_test SET audit = 1 WHERE id = xxxxx"}]'
        :return: self
        """
        sql_list = eval(sql)
        logger.info(f'要执行的update_sql为:{sql}')
        for sql in sql_list:
            try:
                self.cur.execute(sql['sql'])
                self.conn.commit()
                logger.info("数据库更新成功！")
            except:
                self.conn.rollback()
                logger.exception("数据库更新失败！")
        return self

    def get_data(self,sql,size=1):
        """
        获取sql执行后数据
        :param sql:
        :param size: 指定游标获取结果条数
        :return:
        """
        count = self.get_count(sql)
        if count > 0:
            if count == 1:
                res = self.cur.fetchone()
            elif count == -1:
                res = self.cur.fetchall()
            elif count > 1:
                res = self.cur.fetchmany(size=size)
            else:
                res = False
                logger.warning(f'不支持获取size为:{size}的数据')
            logger.info(f'获取到的sql结果数据为：\n{res}')
            return res
        else:
            logger.info(f'执行{sql}以后的结果条数是:0')


    def close_connect(self):
        """
        关闭数据库连接
        :return:
        """
        self.cur.close()
        self.conn.close()
        logger.info('数据库连接已关闭！')