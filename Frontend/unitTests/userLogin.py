from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
import time

#initializing chrome driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#acccessing TwinklTales home page
driver.get("https://twinkle-tales-3c29.vercel.app/")


#exception handling to check the status of test
try:
    #seraching for login button and clicking the login up button
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"form-button_link__gA41G"))
    )

    input_element = driver.find_element(By.CLASS_NAME,"form-button_link__gA41G")
    input_element.click()
    
    email = "akinduusliyanage@gmail.com"
    password = "Akindu@203425"

    #searching for email field andinputting email address
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID,"email"))
    )
    emailId = driver.find_element(By.ID,"email")
    emailId.send_keys(email)

    #searching for password field and inputting password
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID,"password"))
    )
    passwordId = driver.find_element(By.ID,"password")
    passwordId.send_keys(password)


    #searching for login button field and clicking login button
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"form-button_link__gA41G"))
    )
    submit = driver.find_element(By.CLASS_NAME,"form-button_link__gA41G")
    submit.click()

    #searching for profile button and clicking profile button
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"cl-userButtonTrigger"))
    )
    submit = driver.find_element(By.CLASS_NAME,"cl-userButtonTrigger")
    submit.click()

    time.sleep(15)
    print(Fore.GREEN+"\nPass")
    driver.quit()

except:
    print(Fore.RED+ "\nFail")
    time.sleep(10)