import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.checkOut import CheckOutPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOut = homePage.home_form()

        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
        add_cart = checkOut.add_cart_items()
        price = checkOut.add_cart_prices()
        item_names = checkOut.add_cart_item_names()

        log.info(f"Details ,length Add_cart= {len(add_cart)},len Price = {len(price)}, len items_names{len(item_names)}")
        for i in range(0, 4):
            add_cart[i].click()

        time.sleep(1)
        confirm_page = checkOut.checkout_page()
        time.sleep(2)
        final_cart_items = confirm_page.final_cart_items()
        price = confirm_page.final_price().text
        list_items = confirm_page.final_list_items()
        cost = ''
        for i in range(0, len(list_items)):
            cost += list_items[i].text
        print(cost)
        new_cost = cost.split('₹. ')
        new_cost.remove('')
        print(new_cost)
        k = []
        for i in new_cost:
            j = i.replace(' ', '')
            k.append(j)
        print(f"K = {k}")
        print(price)
        sum = 0
        for i in k:
            sum += int(i)

        print(type(sum))

        total = confirm_page.check_total()
        new_total = total.replace('₹. ', '')
        print(type(new_total))
        print(f"new_total={new_total} & sum={sum}")
        assert sum == int(new_total), "Match"

        wait = WebDriverWait(self.driver, 5)
        purchase = confirm_page.checkout_confirm()
        input_search = purchase.country_name()
        input_search.send_keys("ind")
        time.sleep(2)
        input_text_country = input_search.get_attribute("value")

        country_count = purchase.countries_count()

        for i in range(0, len(country_count)):
            if country_count[i].text == "Indonesia":
                country_count[i].click()

        time.sleep(5)
        message_text = purchase.validation_page()

        assert "Success" in message_text

        #Take step screenshot code
        self.driver.get_screenshot_as_file("screenshot.png")
        print("Add line1 ")
        print("Add line 2")
        print("Add line 3")
        print("Add line 4")



