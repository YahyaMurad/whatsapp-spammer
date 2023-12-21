import argparse
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def send_messages(contact_name, message, num_times):
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    sleep(20)

    user = driver.find_element(By.XPATH, "//*[contains(text(), '" + contact_name + "')]")
    user.click()

    for _ in range(num_times):
        actions = ActionChains(driver)
        actions.send_keys(message, Keys.ENTER)
        actions.perform()

    while True:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send messages on WhatsApp using Selenium.")
    parser.add_argument("--name", required=True, help="Name of the contact")
    parser.add_argument("--word", required=True, help="Word to send")
    parser.add_argument("--times", type=int, required=True, help="Number of times to send the word")

    args = parser.parse_args()

    send_messages(args.name, args.word, args.times)
