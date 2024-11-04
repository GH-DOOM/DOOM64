from re import match as rematch
from selenium import webdriver
from dotenv import load_dotenv
from api.methods import *
import pygetwindow as gw
from os import getenv
import pyautogui
import win32gui
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

hwnd = win32gui.FindWindow(None, window_name)
def getScreenshot():
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    screenshot = pyautogui.screenshot(region=(left+10, top+40, width-20, height-50))
    return screenshot.resize((52, 7))

exit_key = getenv("EXIT_KEY")
while True:
    if keyboard.is_pressed(exit_key):
        print("Exit key pressed, exiting...")
        exit()

    browser.displayImage(getScreenshot())