import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Download_BOM
import move_file
import combine_BOM

#loading BOM list for searching
Upload_ME_List = Download_BOM.Run_ME_BOM("上課檔案/Day16/BOM_download.xlsx")
print(Upload_ME_List)

#selenium init
driver = webdriver.Chrome()
#link to web
driver.get("https://material.ui.com/dashboard/approve")
driver.implicitly_wait(1)

#email, pw input
email_input = driver.find_element(By.NAME,'user')
email_input.clear()
email_input.send_keys("aimee.chen@ui.com")
pwd_input = driver.find_element(By.NAME,'password')
pwd_input.clear()
pwd_input.send_keys("Kikiintw2013")
#click login btn
login_btn = driver.find_element(By.CLASS_NAME,"button__VCR3r9bC")
login_btn.click()
#click other methods btn for email va
other_methods_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CLASS_NAME, "css-vwwxf9")))
other_methods_btn.click()

#select email as va method
email_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CLASS_NAME, "css-1kupspz")))
email_btn.click()

#wait for code & click trush btn
trust_btn = WebDriverWait(driver, 30).until(
EC.element_to_be_clickable((By.CLASS_NAME, "button__VCR3r9bC")))
trust_btn.click()

#loop through Bom list
for targer_BOM_no in Upload_ME_List:

    #enter item searching page
    parts_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "component__rHEvxowz")))
    parts_btn = driver.find_elements(By.CLASS_NAME,"component__rHEvxowz")[1]
    parts_btn.click()

    #enter Bom no to searching box
    ME_BOM_PN = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "toolbarInput__gJcHJw7V")))
    ME_BOM_PN.send_keys(targer_BOM_no[:-3])

    #link to target item page
    ME_PN = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, f"[title='{targer_BOM_no[:-3]}']")))
    ME_PN = ME_PN.find_element(By.TAG_NAME, 'a')
    item_link = ME_PN.get_attribute('href')
    driver.get(item_link+'/details')
    
    #click on bill btn
    Bill_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'tab__nBdbJVQs')))
    Bill_btn = driver.find_elements(By.CLASS_NAME, 'tab__nBdbJVQs')[1]
    Bill_btn.click()

    def downlad_process():
        #click on export btn
        export_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/button')))
        export_btn.click()

        #target on modal
        modal = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'modal__jY8jkXxJ')))
        arrow_btn = modal.find_element(By.CLASS_NAME, 'dropdownArrow__xsesnvVh')
        arrow_btn.click()

        #select on default option
        default_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'dropdownOptions_default')))
        default_option.click()

        #click export btn
        export = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'primary__VCR3r9bC')))
        export.click()
        time.sleep(2)

    #click on BOM version select arrow btn
    drop_down_arrow = driver.find_element(By.CLASS_NAME, 'dropdownArrow-light')
    drop_down_arrow.click()
    BOM_no = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'options__Tn64umPB')))
    time.sleep(1)
    BOM_no = BOM_no.find_elements(By.TAG_NAME, 'li')
    download = False
    #va if effective is latest version
    for i in range(len(BOM_no)):
        print(f'cur:{BOM_no[i].text}')
        if 'Effective' in BOM_no[i].text:
            print(f'found cur:{BOM_no[i].text}')
            if i == 0: break
            download = True
            BOM_no[i].click()
            downlad_process()
            break
    if not download:
        downlad_process()

driver.quit()

move_file.move_file('上課檔案/Day16/source')
combine_BOM.combine_BOM('上課檔案/Day16/BOM_file')