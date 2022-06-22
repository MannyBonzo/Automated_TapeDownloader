from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from alright import WhatsApp
import time
import glob
import os
import time

def main():
    msgCode = input("Message Code? ")
    get_message(msgCode)
    time.sleep(1)
    send_message()

def get_message(date):
    options = FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox()
    driver.get("https://branham.org/MessageAudio")

    print("searching...")
    search_box = driver.find_element(By.NAME, "ctl00$main$criteria")
    search_button = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/div/div[2]/div[2]/div[2]/div[1]/div[2]/a")

    search_box.send_keys(date)
    search_button.click()
    time.sleep(2)
    print("found it...")

    download_button = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/div/div[2]/div[2]/div[4]/div/div[2]/span/div[1]/div/div[3]/div[2]/a")
    download_button.click()
    print("downloading, standby...")

    time.sleep(30)
    print("download completed...")
    driver.quit()

def send_message():
    options = ChromeOptions()
    options.add_argument("--headless")
    #Checks for latest Downloaded Message
    list_of_files = glob.glob("C:/Users/smann/Downloads/*.m4a")
    latest_file = max(list_of_files, key=os.path.getmtime)
    print(latest_file)

    messenger = WhatsApp()
    messenger.find_by_username("Randall Barnes")
    messenger.send_file(latest_file)
    time.sleep(10)
    docName = latest_file[25:]
    messenger.send_message("Here is the message, " + docName)
    time.sleep(10)

main()

