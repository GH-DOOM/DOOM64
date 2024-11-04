import api.colorutil as colorutil
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self, driver:webdriver) -> None:
        self.driver = driver

    def changePixelColor(self, x:int, y:int, color:str):
        box = self.driver.find_element(By.ID, f"contribution-day-component-{y}-{x}")
        self.driver.execute_script(f"arguments[0].setAttribute('style', 'width:11px;outline:none;background-color: {color}');", box)
    
        """
        width: 11px;
        outline: none;
        background-color: {color};
        """

    def waitForLoad(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'contribution-day-component-0-0')))

    def removeInfos(self):
        # Less to More
        infobox = self.driver.find_element(By.CLASS_NAME, "ContributionCalendar").find_element(By.CLASS_NAME, "width-full")
        self.driver.execute_script("arguments[0].remove();", infobox)

    def removeLabels(self):
        # Nov, Dec, Jan... Mon, Wed, Fri...
        for element in self.driver.find_elements(By.CLASS_NAME, "ContributionCalendar-label"):
            self.driver.execute_script("arguments[0].remove();", element)

    def displayImage(self, img:Image):
        for x in range(52):
            for y in range(7):
                self.changePixelColor(x,y, colorutil.rgb_to_hex(img.getpixel((x,y))))

    def hideCurrentWeek(self):
        for y in range(7):
            try:
                self.changePixelColor(52, y, "#0D1117") # Github background color
            except:
                pass