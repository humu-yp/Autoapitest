# apitest
基于pytest融入了单例设计模式、数据驱动思想、定制化allure测试报告实现的接口自动化测试

# 介绍

技术栈 python3 + pytest + Yaml + allure + jenkins

涉及第三方库 request、re、faker、pymysql、loguru

# 项目架构说明：

· common：公共方法封装

· conf：配置文件存储

· data：存放yaml测试用例文件

· outputs：存放输出内容 如：allure可解析文件、allure报告、xml结果文件

· test_cases：用例层，单接口/业务流接口的拼接

· DockerFile：集成docker执行

· conftest：pytest固定用法，定制化fixture

· pytest.ini：pytest固定用法,用来存储标签

· test_templates.html：用于集成Jenkins后发送邮件模版

· main.py：执行入口
