from selenium.webdriver.common.by import By

from pageObjects.purchase import Purchase


class Confirm:

    final_items = (By.XPATH , "//h4/a")
    price = (By.XPATH , "//tr[1]/td[3]")
    list_item = (By.XPATH ,"//tr/td[3]")
    total_price = (By.XPATH , "//h3/strong")
    checkout = (By.XPATH , "//button[@class='btn btn-success']")

    def __init__(self,driver):
        self.driver = driver

    def final_cart_items(self):
        return self.driver.find_elements(*Confirm.final_items)

    def final_price(self):
        return self.driver.find_element(*Confirm.price)

    def final_list_items(self):
        return self.driver.find_elements(*Confirm.list_item)

    def check_total(self):
        return self.driver.find_element(*Confirm.total_price).text

    def checkout_confirm(self):
        self.driver.find_element(*Confirm.checkout).click()
        purchase = Purchase(self.driver)
        return purchase




