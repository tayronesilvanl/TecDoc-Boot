from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome webdriver with detach option
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Navigate to the TecDoc website
driver.get('https://web.tecalliance.net/tecdocsw/en/login')

# Try to find and click the accept cookies button, and handle the exception if it occurs
try:
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.presence_of_element_located((By.ID, 'ppms_cm_agree-to-all')))
    accept_button.click()
except:
    pass

# Find the login and password input fields, and enter the login credentials
login_input = driver.find_element(By.ID,'userName')
login_input.send_keys('')
password_input = driver.find_element(By.ID,'password')
password_input.send_keys('')

# Click the login button
login_button = driver.find_element(By.XPATH,'//*[@id="full-width-body"]/scrollable-layout/div/div/div[1]/div[2]/div/div/div/full-width-content/div/login-form/div/div/fieldset/div/form/div[5]/div[2]/div/div/button')
login_button.click()
driver.maximize_window()
#espera pagina principal carregar
time.sleep(2)
input_element = driver.find_element(By.ID,"part-search-input")
input_element.clear()
input_element.send_keys('BD-4113')
Btn_Research = driver.find_element(By.XPATH,"/html/body/catalog-host/webcat-root/div[2]/webcat-header/header/div/div/div[2]/div/input-search-options-picker/div/div[4]/button")
Btn_Research.click()



