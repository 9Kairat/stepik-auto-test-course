from selenium import webdriver
import time

try:
    browser=webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    input1=browser.find_element_by_class_name('btn-primary').click()
    window1 = browser.window_handles[0]
    
    window2 = browser.window_handles[1]
    browser.switch_to_window(window2)
    
    #time.sleep(5)

    x=browser.find_element_by_id('input_value').text
    #x=x_element.text
    print(x)

    import math

    def calc(x):
        return math.log(abs(12*math.sin(int(x))))

    y=str(calc(x))

    input2=browser.find_element_by_id('answer').send_keys(y)
    unput3=browser.find_element_by_tag_name('button').click()
  


finally:
    time.sleep(10)
    browser.quit()