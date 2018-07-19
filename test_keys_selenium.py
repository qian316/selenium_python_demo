#conding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 输入框输入内容
driver.find_element_by_id('kw').send_keys("seleniumm")
time.sleep(2)

# 删除输入框输入的内容
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(2)
# 输入空格键 + "教程"
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys("教程")
time.sleep(2)
# ctrl+a 全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(2)

# ctrl+x 剪切
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(2)

# ctrl+v 粘贴
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
time.sleep(2)

# 回车
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()