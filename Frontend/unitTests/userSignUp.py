from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
import time

#initializing chrome driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#acccessing TwinklTales home page
driver.get("https://twinkle-tales-3c29.vercel.app")

#exception handling to check the status of test
try:
    #clicking sign up button
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Sign Up"))
    )
    input_element = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign Up")
    input_element.click()

    #defining and initializing variable for username, email, and password
    username = "itsMeAkindu"
    email = "methsara.20211273@iit.ac.lk"
    password = "Akindu20003"

    #searching for username field and inputting username
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID,"username"))
    )
    usernameId = driver.find_element(By.ID,"username")
    usernameId.send_keys(username)

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
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"form-button_link__gA41G"))
    )
    submit = driver.find_element(By.CLASS_NAME,"form-button_link__gA41G")
    submit.click()
    time.sleep(5)
    print(Fore.GREEN+ "Pass")
    driver.quit()

except:
    print(Fore.RED+ "Fail")
    time.sleep(10)