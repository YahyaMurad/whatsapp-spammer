from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import platform

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")
sleep(20)

user = driver.find_element(By.XPATH, "//*[contains(text(), '" + "Ali Malaysia" + "')]")

user.click()

word = "HELLO"
x = 100

for i in range(x):
    actions = ActionChains(driver)
    actions.send_keys(word, Keys.ENTER)
    actions.perform()

while True:
    pass