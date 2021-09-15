from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser=webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    element= WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100') )
    input1 = browser.find_element_by_id('book').click()

    import math
    x=browser.find_element_by_id('input_value').text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y=calc(x)

    input2=browser.find_element_by_id('answer').send_keys(y)
    input3=browser.find_element_by_id('solve').click()

    
    
    

finally:
    time.sleep(15)
    browser.quit()