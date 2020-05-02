from pages.Setup import setup
from selenium.webdriver.common.by import By
from utilities import settings
import time
from selenium import webdriver

class HomePage(setup):

    get_Temperature = (By.XPATH, '//*[@id="temperature"]')
    Moisturisers_Button = (By.XPATH, '/html/body/div/div[3]/div[1]/a/button')
    SunScreens_Button = (By.XPATH, '/html/body/div/div[3]/div[2]/a/button')

    def NavigateToProductsBasedOnTemperature(self):
        s = settings.App.settings('')
        time.sleep(1)
        temp = self.browser.find_element(*HomePage.get_Temperature)
        import re
        t = re.search(r'\d+', temp.text)[0]
        print(t)
        if int(s.get('tempcutoff')) > int(t):
            self.browser.find_element(*HomePage.Moisturisers_Button).click()
        elif int(s.get('tempcutoff')) < int(t):
            self.browser.find_element(*HomePage.SunScreens_Button).click()
        return t

