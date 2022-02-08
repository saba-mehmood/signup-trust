
from ast import If
import email
from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import re
from yopmail import Yopmail
from config import TestData
import os


#from yopmail import Yopmail


      
    
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://avaxdev.akru.co/")
window_before = driver.window_handles[0]
driver.find_element(By.CLASS_NAME,'primary-btn').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/div/label[1]/span[1]/span[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button').click()
driver.find_element(By.NAME,'firstName').send_keys(TestData.FIRST_NAME)
driver.find_element(By.NAME,'lastName').send_keys(TestData.LAST_NAME)
driver.find_element(By.NAME,'email').send_keys(TestData.EMAIL)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/fieldset/div/label[3]/span[1]/span[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/div[4]/label/span[1]/span[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/button').click()
time.sleep(10)


"""HANDLING ALERT IF EMAIL IS ALREADY REGISTERED"""

try:
  #switch to alert and print pop up text
    element_alert = driver.find_element(By.CLASS_NAME, 'Toastify__toast-body').get_attribute("textContent")
    time.sleep(3)
    print(element_alert)    
    driver.quit()   
except NoSuchElementException:
   
  print("exception handled")
   

"""YOPMAIL"""
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://yopmail.com/en/")
time.sleep(20)
mail_field = driver.find_element(By.CLASS_NAME,'ycptinput')
mail_field.send_keys(Keys.CONTROL, "a")
mail_field.send_keys(Keys.BACKSPACE)
mail_field.send_keys(TestData.EMAIL)
driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
frame_login = driver.switch_to.frame(driver.find_element(By.ID,'ifmail'))
try:
         login_btn= driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
         login_link=driver.find_element(By.LINK_TEXT,'Click here')
         signup_link= driver.find_element(By.LINK_TEXT,'Verify Email')
         if login_btn.is_displayed() and login_btn.is_enabled():
            login_btn.click()  

         elif login_link.is_displayed():
               login_link.click()

         elif signup_link.is_displayed():
               signup_link.click()      
         
         else:
               print("Login Handle")

except:
         continue_signup = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div/div/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/a/b')
      
         if continue_signup.is_displayed():
                continue_signup.click()      
         
         else:
               print("No Login link Found")
driver.close()


""" CONTACT INFO"""

contact_window=driver.switch_to.window(driver.window_handles[1])
# driver.execute_script("window.open()")
time.sleep(8)
#(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[1]/div/div/div/input'))).send_keys(TestData.ADDRESS)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[1]/div/div/div/input').send_keys(TestData.TRUST)
select=Select(driver.find_element(By.NAME,'trustClassification'))
select.select_by_visible_text('Non-Grantor')

select=Select(driver.find_element(By.NAME,'trustType'))
select.select_by_visible_text('Irrevocable')

select= Select(driver.find_element(By.NAME,'industry'))
select.select_by_visible_text('Restaurant')

"""DATE PICKER"""
 
datee = driver.find_element(By.XPATH," //input[contains(@value,'08/18/2004')]")
datee.click()
datee.send_keys(Keys.CONTROL, "a")   
datee.send_keys("08/18/2002")  
time.sleep(4)

select = Select(driver.find_element(By.NAME,'juristdiction'))
select.select_by_visible_text('Ohio')

element = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[7]/div[2]/input').send_keys(TestData.EIN)
#driver.execute_script("arguments[0].scrollIntoView()", element)


"""SCROLLING MID OF THE PAGE"""
#driver.execute_script("scrollBy(10,+100);")


"""UPLOAD DOC"""
driver.find_element(By.NAME,'file').send_keys("C://Users/jawad/Downloads/Performa wise.pdf")
driver.find_element(By.NAME,'file').send_keys("C://Users/jawad/Downloads/test_summary_report.pdf")

"""TRUST ADDRESS"""
driver.find_element(By.NAME,'address').send_keys(TestData.ADDRESS_LINE_1)
driver.find_element(By.NAME,'city').send_keys(TestData.CITY)
select=Select(driver.find_element(By.NAME,'stateName'))
select.select_by_visible_text('Alabama')
driver.find_element(By.NAME,'zipCode').send_keys(TestData.ZIP_CODE)



""" REPESENTATIVE INFORMAION"""
select=Select(driver.find_element(By.NAME,'title'))
select.select_by_visible_text('CEO')
driver.find_element(By.NAME,'firstName').send_keys(TestData.FIRST_NAME_REPRESENTATIVE)
driver.find_element(By.NAME,'lastName').send_keys(TestData.LAST_NAME_REPRESENTATIVE)
driver.find_element(By.NAME,'email').send_keys(TestData.EMAIL_REPRESENTATIVE)
driver.find_element(By.NAME,'address1').send_keys(TestData.ADDRESS_REPRESENTATIVE)


"""UPLOAD REPRESENATIVE PERSONAL INFORMATION"""
select = Select(driver.find_element(By.NAME,'personalIdType'))
select.select_by_visible_text('Passport')
driver.find_element(By.NAME,'file').send_keys("C://Users/jawad/Downloads/Roofstock.png")
driver.find_element(By.NAME,'city2').send_keys(TestData.CITY_REPRESENTATIVE)
select=Select(driver.find_element(By.NAME,'state2'))
select.select_by_visible_text('Alabama')
driver.find_element(By.NAME,'postalCode').send_keys(TestData.ZIP_CODE)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[23]/input').send_keys(TestData.SSN)
driver.find_element(By.NAME,'number').send_keys(TestData.PHONE_NO)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[24]/div/div/div[2]/button').click()
time.sleep(10)

""" OTP"""

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[2])
driver.get(TestData.OTP)

otp_value= driver.find_element(By.XPATH,'/html/body/pre')

"""USING REGULAR EXPRESSION TO REMOVING TEXT FROM SENTENCE AND GETTING ONLY NUMBERS"""
value = int(re.sub(r"[^\d.]", "", otp_value.text))

"""GETTING LAST 4 NUMBERS FROM WHOLE SENTENCE"""
code=int(str(value)[-4:])
print("value: %s" % code)
driver.close()

"""SWICHING BACK TO CONTACT INFO AND ENTER OTP NUMBER"""
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.NAME,'otp').send_keys(code)

"""DATE PICKER"""
datee = driver.find_element(By.XPATH,"//input[contains(@value,'02/08/2004')]")
datee.click()
datee.send_keys(Keys.CONTROL, "a")   
datee.send_keys("08/18/2002")  
time.sleep(4)

driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[2]/div/button').click()
time.sleep(15)
"""SKIP STEP"""
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button')).click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button').click()
time.sleep(4)

"""VERIFY STEP"""
driver.find_element(By.NAME,'point1').click()
driver.find_element(By.NAME,'point2').click()
driver.find_element(By.NAME,'point3').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/div[2]/div/div/button').click()
time.sleep(4)

"""CONNECT WALLET STEP"""
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button').click()
driver.find_element(By.CLASS_NAME,'donwload-btn').click()
time.sleep(2)



"""YOPMAIL"""
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://yopmail.com/en/")
mail_field = driver.find_element(By.CLASS_NAME,'ycptinput')
mail_field.send_keys(Keys.CONTROL, "a")
mail_field.send_keys(Keys.BACKSPACE)
mail_field.send_keys(TestData.EMAIL)
driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
frame_login = driver.switch_to.frame(driver.find_element(By.ID,'ifmail'))
try:
         login_btn= driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
         login_link=driver.find_element(By.LINK_TEXT,'Click here')
         if login_btn.is_displayed() and login_btn.is_enabled():
            login_btn.click()

         elif login_link.is_displayed():
               login_link.click()
         
         else:
               print("Login Handle")

except:

         signup_link= driver.find_element(By.LINK_TEXT,'Verify Email')
         if signup_link.is_displayed():
               signup_link.click()
               print(driver.title)
         
         else:
               print("No Login link Found")
time.sleep(4)

driver.switch_to.window(driver.window_handles[1])
time.sleep(40) 
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[3]/button').click()

"""HANDLE ALERT"""
try:
  #switch to alert and print pop up text
 element = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body'))).get_attribute("textContent")
 print (element)
except NoAlertPresentException:
  print("exception handled")

print("Rest of the programm")


