from selenium import webdriver
import time
import math


try:
    browser=webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    input1=browser.find_element_by_class_name('btn-primary')
    
    
    input1.click()
    allert=browser.switch_to.alert
    allert.accept()

    input2= browser.find_element_by_id("answer")
    input3= browser.find_element_by_class_name("btn-primary")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    input2.send_keys(y)

    
    input3.click()




finally:
    time.sleep(5)
    browser.quit()