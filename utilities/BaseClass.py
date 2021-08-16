from selenium.webdriver.support.select import Select
import logging
import inspect
import pytest
@pytest.mark.usefixtures("setup")


class BaseClass:

    def select_class(self,locator,text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def getLogger(self):
       loggerName = inspect.stack()[1][3]
       logger =  logging.getLogger(loggerName)
       fileHandler = logging.FileHandler('logfile.log')
       formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
       fileHandler.setFormatter(formatter)

       logger.addHandler(fileHandler)
       logger.setLevel(logging.DEBUG)
       return logger
