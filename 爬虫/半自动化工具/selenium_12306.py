from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
browser = webdriver.Chrome(r"I:\Anaconda\Scripts\chromedriver")
# browser.get("https://kyfw.12306.cn/otn/leftTicket/init")
# login = browser.find_element_by_id("login_user")
# login.click()
# username = "15871687941"
# password = "asd2743075"
# input_user = browser.find_element_by_id("username")
# input_user.send_keys(username)
# input_password = browser.find_element_by_id("password")
# input_password.send_keys(password)
# 验证码
# 操作
browser.get("https://kyfw.12306.cn/otn/leftTicket/init")
fromStationText = browser.find_element_by_id("fromStationText")
toStationText = browser.find_element_by_id("toStationText")
date = browser.find_element_by_id("train_date")
student = browser.find_element_by_id("sf2")
sleep(5)
fromStationText.click()
fromStationText.send_keys("襄阳")
fromStationText.send_keys(Keys.ENTER)
sleep(5)
toStationText.click()
toStationText.send_keys("武汉")
toStationText.send_keys(Keys.ENTER)
sleep(5)
date.click()
browser.find_element_by_xpath('//*[@id="date-list"]/li[@name="2018-08-15"]').click()
select = browser.find_element_by_id("query_ticket")
select.click()
sleep(5)
browser.close()