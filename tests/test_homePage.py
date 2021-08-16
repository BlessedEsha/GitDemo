import pytest
import time

from TestData.homePageTestData import HomePageTestData
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_homePage(self ,datasetup2 ):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(datasetup2[0]["firstname"])
        homepage.getEmail().send_keys(datasetup2[0]["email"])
        homepage.getPassword().send_keys("pwd")
        time.sleep(3)
        self.select_class(homepage.getGender(),datasetup2[0]["gender"])
        homepage.clickSubmit().click()
        log = self.getLogger()
        log.info("Checking assertion for " + homepage.getmessage())
        assert "Success" in homepage.getmessage()

    @pytest.fixture(params=HomePageTestData.test_homePage_Data)
    def datasetup(self , request):
        return request.param

    @pytest.fixture(params=[HomePageTestData.get_testData("TestCaseName1"),HomePageTestData.get_testData("TestCaseName2")])
    def datasetup2(self, request):
        return request.param


