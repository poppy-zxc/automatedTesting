# -*- coding:utf-8 -*-

import pytest
import os

if __name__ == "__main__":
    pytest.main() # 程序入口
    os.system("allure serve temps/allure") # 生成html测试报告


