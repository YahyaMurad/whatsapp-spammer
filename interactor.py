import platform
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize driver
driver = webdriver.Chrome() # Add driver path

driver.get("https://web.whatsapp.com")
sleep(20)

# Change NAME OF RECIPIENT
user = driver.find_element(By.XPATH, "//*[contains(text(), '" + "NAME OF RECIPIENT" + "')]")

user.click()

word = "HELLO" # Word that is being sent
x = 100 # Number of times it is being set

for i in range(x):
    actions = ActionChains(driver)
    actions.send_keys(word, Keys.ENTER)
    actions.perform()

while True:
    pass
