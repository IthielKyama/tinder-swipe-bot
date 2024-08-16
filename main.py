from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/app/recs")

# Accept cookies.
time.sleep(2)
accept_cookies = driver.find_element(By.XPATH, '//*[@id="q-612006581"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()

# Log in.
log_in = driver.find_element(By.XPATH, '//*[@id="q-612006581"]/div/div[1]/div/main/div[1]/div/div/div/div/div/'
                                       'header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(3)
fb_login = driver.find_element(By.XPATH, '/html')
fb_login.click()

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)

time.sleep(3)
email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
submit = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
submit.click()

time.sleep(2)
input("Press Enter to confirm.")

driver.switch_to.window(base_window)

# Allow location access.
time.sleep(5)
allow_loc_access = driver.find_element(By.XPATH, '//*[@id="q1954579639"]/div/div/div/div/div[3]/button[1]')
allow_loc_access.click()

# Reject notifications.
time.sleep(2)
reject = driver.find_element(By.XPATH, '//*[@id="q1954579639"]/div/div/div/div/div[3]/button[2]')
reject.click()

# Swipe left.
time.sleep(10)
swipe_left = driver.find_element(By.XPATH, '//*[@id="q-612006581"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')

for n in range(5):
    try:
        swipe_left.click()
    # except ElementClickInterceptedException:
    #     try:
    #         match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
    #         match_popup.click()
    except NoSuchElementException:
        time.sleep(3)

    time.sleep(10)

driver.quit()
