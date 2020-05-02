from pages.Setup import setup
from selenium.webdriver.common.by import By
from utilities import settings
from pages.HomePage import HomePage
import time
from selenium import webdriver
import rootpath
import re
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = rootpath.detect()
product = {}
pricenaddtocartbuttonrelation = {}
pricenaddtocartbuttonrelationSPF50 = {}
pricenaddtocartbuttonrelationSPF30 = {}
add = {}
titles = []
prices = []
SPF50prices = []
SPF30prices = []

class Products(setup):

    g = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/p[1]')
    h = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/p[1]')
    products = (By.NAME, "text-center col-4")
    addtoCart = (By.XPATH, "/html/body/nav/ul/button")
    cartItem1 = (By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr[1]/td[2]")
    cartItem2 = (By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr[2]/td[2]")
    sortedPrices = []
    cartTotal = (By.XPATH, "//*[@id='total']")
    paymentLink = (By.XPATH, "/html/body/div[1]/div[3]/form/button/span")

    def addProductsToCart(self, temperture):

        s = settings.App.settings('')
        if s['tempcutoff'] > temperture:

            time.sleep(10)

            for i in range(1, 4):
                s = '/html/body/div[1]/div[2]/div[' + str(i) + ']/p[1]'
                priceoftheproduct = '/html/body/div[1]/div[2]/div[' + str(i) + ']/p[2]'
                c = self.browser.find_element_by_xpath(s)
                x = self.browser.find_element_by_xpath(priceoftheproduct)
                print(c.text)
                matchAloe = re.search(r'\bAloe\b', str(c.text))
                if matchAloe:
                    titles.append(c.text)
                    product[c.text] = re.findall("\d+", x.text)[0]
                    AddToCartbutton = '/html/body/div[1]/div[2]/div[' + str(i) + ']/button'
                    prices.append(product[c.text])
                    pricenaddtocartbuttonrelation[re.findall("\d+", x.text)[0]] = AddToCartbutton

                else:
                    print("not a desired product")

            for j in range(1, 4):
                s1 = '/html/body/div[1]/div[3]/div[' + str(j) + ']/p[1]'
                priceoftheproduct1 = '/html/body/div[1]/div[3]/div[' + str(j) + ']/p[2]'
                c1 = self.browser.find_element_by_xpath(s1)
                x1 = self.browser.find_element_by_xpath(priceoftheproduct1)
                print(c1.text)
                matchAloe1 = re.search(r'\bAloe\b', str(c1.text))
                if matchAloe1:
                    product[c1.text] = re.findall("\d+", x1.text)[0]
                    AddToCartbutton1 = '/html/body/div[1]/div[3]/div[' + str(j) + ']/button'
                    prices.append(product[c1.text])
                    pricenaddtocartbuttonrelation[re.findall("\d+", x1.text)[0]] = AddToCartbutton1

                else:
                    print("not a desired product")

            print(sorted(prices))
            sortedPrices = sorted(prices)
            pp = json.dumps(product)
            print(pp)
            print(pricenaddtocartbuttonrelation)
            if (len(prices) > 1):
                self.browser.find_element_by_xpath(pricenaddtocartbuttonrelation[sortedPrices[0]]).click()
                self.browser.find_element_by_xpath(pricenaddtocartbuttonrelation[sortedPrices[1]]).click()
            else:
                self.browser.find_element_by_xpath(pricenaddtocartbuttonrelation[sortedPrices[0]]).click()
            time.sleep(2)
            self.browser.find_element(*Products.addtoCart).click()
            c1 = self.browser.find_element(*Products.cartItem1)
            c2 = self.browser.find_element(*Products.cartItem2)
            print(c1.text)
            print(c2.text)

            if c1.text == sortedPrices[0] and c2.text == sortedPrices[1]:
                total = int(sortedPrices[0]) + int(sortedPrices[1])
                print(total)
                ctotal = self.browser.find_element(*Products.cartTotal)
                ct = re.findall("\d+", ctotal.text)[0]
                print(ct)
                if int(total) == int(ct):
                    self.browser.find_element(*Products.paymentLink).click()
                else:
                    print("total is wrong")

            time.sleep(10)

        elif s['tempcutoff'] < temperture:
            for i in range(1, 4):
                s = '/html/body/div[1]/div[2]/div[' + str(i) + ']/p[1]'
                priceoftheproduct = '/html/body/div[1]/div[2]/div[' + str(i) + ']/p[2]'
                c = self.browser.find_element_by_xpath(s)
                x = self.browser.find_element_by_xpath(priceoftheproduct)
                print(c.text)
                matchAloe = re.search(r'\bSPF-50\b', str(c.text))
                if matchAloe:
                    titles.append(c.text)
                    product[c.text] = re.findall("\d+", x.text)[0]
                    AddToCartbutton = '/html/body/div[1]/div[2]/div[' + str(i) + ']/button'
                    SPF50prices.append(product[c.text])
                    pricenaddtocartbuttonrelationSPF50[re.findall("\d+", x.text)[0]] = AddToCartbutton

                else:
                    print("not a desired product")

            for j in range(1, 4):
                s1 = '/html/body/div[1]/div[3]/div[' + str(j) + ']/p[1]'
                priceoftheproduct1 = '/html/body/div[1]/div[3]/div[' + str(j) + ']/p[2]'
                c1 = self.browser.find_element_by_xpath(s1)
                x1 = self.browser.find_element_by_xpath(priceoftheproduct1)
                print(c1.text)
                matchAloe1 = re.search(r'\bSPF-50\b', str(c1.text))
                if matchAloe1:
                    product[c1.text] = re.findall("\d+", x1.text)[0]
                    AddToCartbutton1 = '/html/body/div[1]/div[3]/div[' + str(j) + ']/button'
                    SPF50prices.append(product[c1.text])
                    pricenaddtocartbuttonrelationSPF50[re.findall("\d+", x1.text)[0]] = AddToCartbutton1

                else:
                    print("not a desired product")

            for k in range(1, 4):
                s2 = '/html/body/div[1]/div[2]/div[' + str(k) + ']/p[1]'
                priceoftheproduct2 = '/html/body/div[1]/div[2]/div[' + str(k) + ']/p[2]'
                c2 = self.browser.find_element_by_xpath(s2)
                x2 = self.browser.find_element_by_xpath(priceoftheproduct2)
                print(c2.text)
                matchAloe2 = re.search(r'\bSPF-30\b', str(c2.text))
                if matchAloe2:
                    titles.append(c2.text)
                    product[c2.text] = re.findall("\d+", x2.text)[0]
                    AddToCartbutton2 = '/html/body/div[1]/div[2]/div[' + str(k) + ']/button'
                    SPF30prices.append(product[c2.text])
                    pricenaddtocartbuttonrelationSPF30[re.findall("\d+", x2.text)[0]] = AddToCartbutton2

                else:
                    print("not a desired product")

            for l in range(1, 4):
                s3 = '/html/body/div[1]/div[3]/div[' + str(l) + ']/p[1]'
                priceoftheproduct3 = '/html/body/div[1]/div[3]/div[' + str(l) + ']/p[2]'
                c3 = self.browser.find_element_by_xpath(s3)
                x3 = self.browser.find_element_by_xpath(priceoftheproduct3)
                print(c3.text)
                matchAloe3 = re.search(r'\bSPF-30\b', str(c3.text))
                if matchAloe3:
                    product[c3.text] = re.findall("\d+", x3.text)[0]
                    AddToCartbutton3 = '/html/body/div[1]/div[3]/div[' + str(l) + ']/button'
                    SPF30prices.append(product[c3.text])
                    pricenaddtocartbuttonrelationSPF30[re.findall("\d+", x3.text)[0]] = AddToCartbutton3

                else:
                    print("not a desired product")

            print(sorted(SPF50prices))
            sortedSPF50Prices = sorted(SPF50prices)
            sortedSPF30Prices = sorted(SPF30prices)
            pp = json.dumps(product)
            print(pp)
            print(pricenaddtocartbuttonrelation)
            self.browser.find_element_by_xpath(pricenaddtocartbuttonrelationSPF50[sortedSPF50Prices[0]]).click()
            self.browser.find_element_by_xpath(pricenaddtocartbuttonrelationSPF30[sortedSPF30Prices[0]]).click()
            time.sleep(2)
            self.browser.find_element(*Products.addtoCart).click()
            c1 = self.browser.find_element(*Products.cartItem1)
            c2 = self.browser.find_element(*Products.cartItem2)
            print(c1.text)
            print(c2.text)

            if c1.text == sortedSPF50Prices[0] and c2.text == sortedSPF30Prices[0]:
                total = int(sortedSPF50Prices[0]) + int(sortedSPF30Prices[0])
                print(total)
                ctotal = self.browser.find_element(*Products.cartTotal)
                ct = re.findall("\d+", ctotal.text)[0]
                print(ct)
                if int(total) == int(ct):
                    self.browser.find_element(*Products.paymentLink).click()
                else:
                    print("total is wrong")

            time.sleep(10)















