'''
@Filename: automatedTesting -> test_web
@Author: AnnieZhang
@Date: 2023/1/28 10:10
'''

import pytest
from core.pom import *
from core.datas import read_csv, read_excel

class TestWeb: # 测试套件


    def test_scroll(self, driver):
        driver.execute_script("window.scrollTo(0,200)")

    @pytest.mark.parametrize(
        "data",
        read_csv(r"C:\Users\anning\PycharmProjects\automatedTesting\datas\search.csv")
    )
    def test_a(self, driver, data):
        import time
        # time.sleep(2)
        print("i am here")
        pass

    @pytest.mark.parametrize(
        "username, password, msg",
        read_excel(r"C:\Users\anning\PycharmProjects\automatedTesting\datas\annie.xlsx")
    )
    def test_login(self, driver, username, password, msg):
        print(username)