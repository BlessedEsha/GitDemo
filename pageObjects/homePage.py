from selenium.webdriver.common.by import By

from pageObjects.checkOut import CheckOutPage


class HomePage:
    form_name = (By.NAME,"name")
    shop_link = (By.XPATH , "//ul[@class='navbar-nav']/li[2]")
    email = (By.NAME , "email")
    password = (By.ID , "exampleInputPassword1")
    gender = (By.ID , "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR , "input[value='Submit']")
    message = ((By.XPATH , "//div[@class='container']/div[2]"))

    def __init__(self,driver):
        self.driver = driver

    def getName(self):
        return self.driver.find_element(*HomePage.form_name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getmessage(self):
        return self.driver.find_element(*HomePage.message).text


    def home_form(self):
        #  self.driver.find_element_by_name("name").send_keys("esha")
        self.driver.find_element(*HomePage.form_name).send_keys("esha")
        self.driver.find_element(*HomePage.shop_link).click()

        checkout = CheckOutPage(self.driver)
        return checkout




