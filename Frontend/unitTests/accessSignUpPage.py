from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://twinkle-tales-3c29.vercel.app/")
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Sign Up"))
    )

    input_element = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign Up")
    input_element.click()
    time.sleep(5)
    print(Fore.GREEN+"\nPass")
    driver.quit()

except:
    print(Fore.RED+ "\nFail")