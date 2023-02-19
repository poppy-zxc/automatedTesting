import pytest
from webdriver_helper import get_webdriver


@pytest.fixture(scope="session")
def driver():
    d = get_webdriver() # 打开浏览器
    # d.get("http://baidu.com")
    d.get("https://www.hao123.com/?src=from_pc")
    yield d
    d.quit() # 关闭浏览器