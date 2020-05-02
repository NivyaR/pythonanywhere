from pages.Setup import setup
from selenium.webdriver.common.by import By
from utilities import settings
from pages.HomePage import HomePage
from pages.ProductsPage import Products
import time
from selenium import webdriver
import rootpath
import re
import json

class cartpage(setup):

    cartItem1 = (By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr[1]/td[2]")
    cartItem2 = (By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr[2]/td[2]")
    cartTotal = (By.XPATH, "//*[@id='total']")
    paymentLink = (By.XPATH, "/html/body/div[1]/div[3]/form/button/span")
    paymentFrame = (By.NAME, "stripe_checkout_app")
    Email = (By.XPATH, "/html/body/div[2]/section/span[2]/div/div/main/form/div/div/div/div/div/div[1]/div[1]/div/div/div/fieldset/span/div/div[1]/input")
    Card = (By.XPATH, "/html/body/div[2]/section/span[2]/div/div/main/form/div/div/div/div/div/div[1]/div[2]/fieldset/div[1]/div[1]/span/span[1]/div/div[1]/input")
    expiry = (By.XPATH, "/html/body/div[2]/section/span[2]/div/div/main/form/div/div/div/div/div/div[1]/div[2]/fieldset/div[1]/div[2]/div[1]/div[1]/input")
    cvv = (By.XPATH, "/html/body/div[2]/section/span[2]/div/div/main/form/div/div/div/div/div/div[1]/div[2]/fieldset/div[1]/div[2]/div[2]/div[1]/input")
    payButton = (By.XPATH, "/html/body/div[2]/section/span[2]/div/div/main/form/div/div/div/div/div/div[1]/div[2]/fieldset/div[1]/div[2]/div[2]/div[1]/input")
    zipcode = (By.XPATH, "/html/body/div[2]/section/span[2]/div/div/main/form/div/div/div/div/div/div[1]/div[2]/fieldset/div[2]/div/div/div/div/div[1]/input")
    paymentsuccess = (By.XPATH, "/html/body/div/div[1]/h2")

    def doPayment(self):

        s = settings.App.settings('')
        f = self.browser.find_element(*cartpage.paymentFrame)
        self.browser.switch_to.frame(f)
        self.browser.find_element(*cartpage.Email).send_keys(s['email'])
        self.browser.find_element(*cartpage.Card).send_keys(s['card'])
        self.browser.find_element(*cartpage.expiry).send_keys(s['expiry'])
        self.browser.find_element(*cartpage.cvv).send_keys(s['cvv'])
        self.browser.find_element(*cartpage.zipcode).send_keys("54321")
        self.browser.find_element(*cartpage.payButton).click()
        self.browser.switch_to.default_content()
        time.sleep(3)
        x = self.browser.find_element(*cartpage.paymentsuccess)
        if (x.text == "PAYMENT SUCCESS"):
            print("PAYMENT SUCCESS")







