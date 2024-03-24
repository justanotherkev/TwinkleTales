from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import Fore
import time

#initializing chrome driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    #acccessing TwinklTales home page
    driver.get("https://twinkle-tales-3c29.vercel.app/")
    time.sleep(10)
    print(Fore.GREEN + "\nPass")
except:
    print(Fore.RED + "Fail")
