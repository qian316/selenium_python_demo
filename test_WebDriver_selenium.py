#conding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# id定位
# driver.find_element_by_id("kw").clear()
# time.sleep(3)
# driver.find_element_by_id("kw").send_keys("selenium")
# time.sleep(2)
# driver.find_element_by_id("su").click()
# time.sleep(2)


# xpath定位
# driver.find_element_by_xpath("//*[@id='kw']").clear()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='su']").click()
# time.sleep(2)


# submit()方法
# search_text = driver.find_element_by_id('kw')
# search_text.send_keys('selenium')
# search_text.submit()
# time.sleep(2)

# 获取输入框的尺寸
# size = driver.find_element_by_id('kw').size
# print(size)
#
# # 获取百度页面底部的备案信息  //*[@id="bottom_container"]/div/div[2]/div[1]/span/span[1]
text = driver.find_element_by_id('cp').text
print(text)
#
# # 返回元素的属性值，
# attribute = driver.find_element_by_id('kw').get_attribute('type')
# print(attribute)
#
# # 返回元素的结果是否可见，返回的结果为True或False
# result = driver.find_element_by_id('kw').is_displayed()
# print(result)



driver.quit()



