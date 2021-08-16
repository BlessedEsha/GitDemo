import pytest
from selenium import webdriver

#Anything which we want run before test case execution can be put into fixtures
@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    request.cls.driver = driver.close()
