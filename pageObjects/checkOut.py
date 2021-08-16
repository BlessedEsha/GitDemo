from selenium.webdriver.common.by import By

from pageObjects.confirm import Confirm


class CheckOutPage:
    add_cart_item = (By.XPATH,"//button[@class='btn btn-info']")
    add_cart_price = (By.XPATH,"//h5")
    add_cart_item_name = (By.XPATH,"//h4[@class='card-title']")
    checkout = (By.XPATH , "//li[@class='nav-item active']/a")

    def __init__(self,driver):
        self.driver = driver

    def add_cart_items(self):
        return self.driver.find_elements(*CheckOutPage.add_cart_item)

    def add_cart_prices(self):
        return self.driver.find_elements(*CheckOutPage.add_cart_price)


    def add_cart_item_names(self):
        return self.driver.find_elements(*CheckOutPage.add_cart_item_name)

    def checkout_page(self):
        self.driver.find_element(*CheckOutPage.checkout).click()
        confirm = Confirm (self.driver)
        return confirm
