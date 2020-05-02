import unittest
import pytest
import self as self
from selenium import webdriver

from pages import Setup
from pages.HomePage import HomePage
from pages.ProductsPage import Products
from pages.cartPage import cartpage
from pages.Setup import setup
from utilities import settings

s = settings.App.settings('')

class PlaceOrderTest(unittest.TestCase):

    def setUp(self) -> None:
        import rootpath
        path = rootpath.detect()
        if (s['browsers'] == "chrome"):
            self.browser = webdriver.Chrome(path + '/Documents/sandie/weathershopper/drivers/chromedriver')
            self.browser.get(s['url'])
            self.browser.maximize_window()
        elif (s['browsers'] == "firefox"):
            Fp = webdriver.FirefoxProfile(path + '/Documents/sandie/weathershopper/drivers/geckodriver')
            self.browser = webdriver.Firefox(Fp)
            self.browser.get(s['url'])
            self.browser.maximize_window()

    def test_placeOrder(self):
        H = HomePage(self.browser)
        t = H.NavigateToProductsBasedOnTemperature()
        Products(self.browser).addProductsToCart(t)
        cartpage(self.browser).doPayment()

if __name__ == "__main__":
    unittest.main()