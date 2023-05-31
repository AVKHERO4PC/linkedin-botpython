from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
srv = Service('C:/Users/AVK/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(options=options,service=srv)
driver.get('https://www.linkedin.com')
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

#********** LOG IN *************

username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='session_key']")))
password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='session_password']")))


username.send_keys('avkhero4pc@gmail.com')
password.send_keys('Einstein#2004@')

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)


submit_button.click()
#*************** ADD CONTACTS**************************
driver.get('https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=TKA')
time.sleep(2)
all_buttons = driver.find_elements(By.TAG_NAME, "button")
connect_btns = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_btns:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    time.sleep(2)
