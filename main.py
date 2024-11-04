from re import match as rematch
from dotenv import load_dotenv
from api.methods import *
import pygetwindow as gw
from os import getenv
import pyautogui
import keyboard

load_dotenv()

match(getenv("DRIVER").lower()):
    case "firefox": browser = Browser(webdriver.Firefox())
    case "chrome": browser = Browser(webdriver.Chrome())

browser.driver.get("https://github.com/GH-DOOM/")
browser.waitForLoad()

browser.hideCurrentWeek()

window_name = ""
for window in gw.getAllTitles():
    if rematch(rf"{getenv('DOOM_REGEX')}", window):
        window_name = window
if window_name == "":
    print("Unable to find DOOM")
    print("Are you running DOOM 64 ?")
    print("If yes, change DOOM_REGEX in .env")
    exit()

window = gw.getWindowsWithTitle(window_name)[0]
def getScreenshot():
    left, top, width, height = window.left, window.top, window.width, window.height
    img = pyautogui.screenshot(region=(left + 8, top + 31, width - 16, height - 39))
    return img.resize((52, 7))

exit_key = getenv("EXIT_KEY")
while True:
    if keyboard.is_pressed(exit_key):
        print("Exit key pressed, exiting...")
        exit()

    browser.displayImage(getScreenshot())