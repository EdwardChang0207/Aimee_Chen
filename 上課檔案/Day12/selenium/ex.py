from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://google.com')
google_login_btn = driver.find_element(By.CLASS_NAME, 'gb_A')
google_login_btn.click()

google_email_input = driver.find_element(By.NAME,'identifier')
google_email_input.clear()
google_email_input.send_keys('funnycoding@letsfunnycoding.com')
google_login_btn = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe-OWXEXe-k8QpJ')
google_login_btn.click()

google_pwd_input = driver.find_element(By.NAME, 'Passwd')
google_pwd_input.clear()
google_pwd_input.send_keys('')
google_login_btn = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe-OWXEXe-k8QpJ')
google_login_btn.click()

time.sleep(5)
# driver.get("http://selenium.dev")
# driver.implicitly_wait(1)
# title = driver.title
# email_input = driver.find_element(By.NAME, 'user')
# email_input.clear()
# email_input.send_keys('aimee.chen@ui.com')
# login_btn = driver.find_element(By.CLASS_NAME, '')
# login_btn.click()
time.sleep(10)
driver.quit()