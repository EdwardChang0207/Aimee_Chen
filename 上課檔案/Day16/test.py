from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import Download_BOM

Upload_ME_List = Download_BOM.Run_ME_BOM("上課檔案/Day16/BOM_download.xlsx")
print(Upload_ME_List)

driver = webdriver.Chrome()

driver.get("https://material.ui.com/dashboard/approve")
driver.implicitly_wait(1)
title = driver.title
email_input = driver.find_element(By.NAME,'user')
email_input.clear()
email_input.send_keys("aimee.chen@ui.com")
pwd_input = driver.find_element(By.NAME,'password')
pwd_input.clear()
pwd_input.send_keys("Kikiintw2013")
login_btn = driver.find_element(By.CLASS_NAME,"button__VCR3r9bC")
login_btn.click()
time.sleep(3) #
login2_btn = driver.find_element(By.CLASS_NAME,"css-vwwxf9")
login2_btn.click()
time.sleep(3)
email_btn = driver.find_element(By.CLASS_NAME,"css-1kupspz")
email_btn.click()
time.sleep(30)
trust_btn = driver.find_element(By.CLASS_NAME,"button__VCR3r9bC")
trust_btn.click()
time.sleep(5)
parts_btn = driver.find_elements(By.CLASS_NAME,"component__rHEvxowz")[1]
parts_btn.click()
time.sleep(5)
ME_BOM_PN = driver.find_element(By.CLASS_NAME,"toolbarInput__gJcHJw7V")
ME_BOM_PN.send_keys(Upload_ME_List[0][:-3])
time.sleep(2)
ME_PN = driver.find_element(By.CSS_SELECTOR,f"[title='{Upload_ME_List[0][:-3]}']")
ME_PN = ME_PN.find_element(By.TAG_NAME, 'a')
item_link = ME_PN.get_attribute('href')
driver.get(item_link+'/details')
time.sleep(5)
drop_down_arrow = driver.find_element(By.CLASS_NAME, 'dropdownArrow-light')
drop_down_arrow.click()
time.sleep(3)
BOM_no = driver.find_element(By.CLASS_NAME, 'options__Tn64umPB')
time.sleep(1)
BOM_no = BOM_no.find_elements(By.TAG_NAME, 'li')
target_BOM_no = Upload_ME_List[0].split('-')[-1]
target_BOM_no = int(target_BOM_no)
print(target_BOM_no)
for i in BOM_no:
    print(f'cur:{i.text}')
    if i.text.split()[0] == str(target_BOM_no):
        print(f'found cur:{i.text}')
        i.click()
        break
time.sleep(5)

# Rev_list_0 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div")
# Rev_list_0 = Rev_list_0.find_elements(By.TAG_NAME,"div")[1]
# Rev_list_0 = Rev_list_0.find_element(By.TAG_NAME,"ul")
# print(Rev_list_0)

# Rev_list_0 = Rev_list_0.find_element(By.TAG_NAME,"div")
# Rev_list_1 = driver.find_element(By.CLASS_NAME,"inputContainer__Tn64umPB")
# time.sleep(15)
# Rev_list_2 = Rev_list_1.find_element(By.CLASS_NAME,"options__Tn64umPB")
# Rev_list_li = Rev_list_2.find_elements(By.TAG_NAME, "li")
# # for i in Rev_list_li:
#     print(i.find_element(By.TAG_NAME, "div").text)


# driver.quit()