from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
browser = webdriver.Chrome(r"I:\Anaconda\Scripts\chromedriver")
browser.get("http://vip.biancheng.net/")
try:
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "user-info")))
    login_url = browser.find_element_by_link_text("登录")
    login_url.click()
    input_username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    input_password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    input_username.send_keys("***")
    input_password.send_keys("*******")
    button_login = browser.find_element(By.ID, "submit")
    button_login.click()
    index_url = browser.find_element_by_link_text("C语言")
    index_url.click()

    sleep(10)
except NoSuchElementException:
    print("No such element！")
finally:
    browser.quit()