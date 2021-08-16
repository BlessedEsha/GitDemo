from selenium.webdriver.common.by import By


class Purchase:

    country = (By.ID , "country")
    country_count = (By.XPATH , "//div[@class='suggestions']//li")
    checkbox = (By.XPATH , "//div[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH , "//input[@value='Purchase']")
    val_text = (By.XPATH , "//div[@class='container']/app-checkout/div[2]")

    def __init__(self,driver):
        self.driver = driver

    def country_name(self):
        return self.driver.find_element(*Purchase.country)

    def countries_count(self):
        return self.driver.find_elements(*Purchase.country_count)

    def validation_page(self):
        self.driver.find_element(*Purchase.checkbox).click()
        self.driver.find_element(*Purchase.purchase).click()
        return self.driver.find_element(*Purchase.val_text).text



