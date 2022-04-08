from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os
import csv
import random as rd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui



df = pd.read_excel (r'sending_data.xlsx')
capabilities = webdriver.DesiredCapabilities.CHROME
options = Options()
options.add_argument("start-maximized")
# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service()
driver = webdriver.Chrome(desired_capabilities=capabilities,options=chrome_options)
# Selenium Stealth settings
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win64",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )


def login(username,password):
    email = driver.find_element(By.ID,"username")
    email.send_keys(username)
    password1 = driver.find_element(By.ID,'password')
    password1.send_keys(password)
    
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[contains(@class,'LoginForm_input-wrapper-but')]/button[@type='submit']").click()
    
   
def placeadd():
    for i in range(len(df)):
        time.sleep(10)
        driver.find_element(By.XPATH,"//div[@class='index-module_button-add__uLc1X']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//img[@alt="Motori"]/parent::div').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'//p[text()="Accessori auto"]/parent::div').click()
        driver.implicitly_wait(10)
    #selection condition item
        condition = Select(driver.find_element(By.NAME,'item_condition'))
        condition.select_by_index(df['condizione'][i])
        time.sleep(5)
        # select images
        try:
            # import pdb;pdb.set_trace()
            item = driver.find_element(By.XPATH,"//input[@name='fileElem']")
            # driver.execute_script("document.getElementById('fileList').setAttribute('type','text')")
            time.sleep(5)
            item.send_keys("https:\\cdn.britannica.com\46\3346-004-D3BDE016\flag-symbolism-Pakistan-design-Islamic.jpg")
            # pyautogui.press('enter')
            time.sleep(2)
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys(df['imm1'][i])
            time.sleep(2)
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys(df['imm1'][i])
            time.sleep(2)
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys(df['imm1'][i])
            time.sleep(2)
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys(df['imm1'][i])
        except:
            pass
        #sending title
            title = driver.find_element(By.ID,'subject')
            title.send_keys(df['titolo'][i])
        # sending text

            text = driver.find_element(By.ID,'body')
            text.send_keys(df['descrizione'][i])
            time.sleep(3)
        # adding price
            price = driver.find_element(By.ID,'price')
            price.send_keys(str(df['prezzo_vendita'][i]))
        #adding common
            common = driver.find_element(By.ID,'town')
            common.send_keys(df['luogo'][i])
        # adding address
            try:
                address = driver.find_element(By.ID,'address')
                address.send_keys(df['luogo'][i])
            except:
                pass

        # Phone number
            phone = driver.find_element(By.ID,'phone')
            phone.send_keys('123456789')
            time.sleep(4)

            driver.find_element(By.ID,'btnAiSubmit').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID,'btnConfirm').click()
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH,'//button[@type="submit"]').click()



    
if __name__ == "__main__":
    driver.get("https://areariservata.subito.it/login_form")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"didomi-notice-agree-button").click()
    time.sleep(10)
    login('maqsoomahmed98@gmail.com','maqsoom1')
    placeadd()
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@class='index-module_button-add__uLc1X']").click()

    

