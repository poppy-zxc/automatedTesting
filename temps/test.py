# -*- coding:utf-8 -*-

from webdriver_helper import get_webdriver

driver = get_webdriver()
driver.get("http://baidu.com")
input()
driver.quit()

# driver = webdriver.Chrome()
#
# driver.get_screenshot_as_file('1.启动浏览器.png')
# driver.get('https://www.baidu.com/')
# driver.find_element(By.ID)
# driver.maximize_window()
# driver.get_screenshot_as_file('2.最大化百度.png')
# driver.quit()