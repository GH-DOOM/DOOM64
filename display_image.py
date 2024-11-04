from selenium import webdriver
from dotenv import load_dotenv
from api.methods import *
from os import getenv

load_dotenv()

match(getenv("DRIVER").lower()):
    case "firefox": browser = Browser(webdriver.Firefox())
    case "chrome": browser = Browser(webdriver.Chrome())

browser.driver.get("https://github.com/GH-DOOM/")
browser.waitForLoad()

browser.hideCurrentWeek()

img = Image.open(open(getenv("IMAGE_PATH"), "rb"))

browser.displayImage(img)