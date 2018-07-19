#conding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")

# 定位到要悬浮的元素
above = driver.find_element_by_link_text("设置")
# 对定位的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

above = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/span")
# 双击
ActionChains(driver).double_click(above).perform()
