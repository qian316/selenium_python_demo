#conding=utf-8
from  selenium import webdriver

# Chrome谷歌浏览器
driver = webdriver.Chrome()

driver.get("http://m.baidu.com")


#print(driver.title)
print("设置浏览器宽480、高800显示")
driver.set_window_size(480,800)

driver.quit()