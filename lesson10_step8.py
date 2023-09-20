from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, '#price'), '100'))
button_book = browser.find_element(By.CSS_SELECTOR, '#book').click()
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
res = calc(x)
input2 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(res)
solve = browser.find_element(By.CSS_SELECTOR, '#solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", solve)
solve.click()
time.sleep(3)
