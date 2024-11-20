import random
import pytest
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URL
from locators.scooter_order_locators import TestOrderLocators


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Firefox()
    driver.get(URL)
    close_banner_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((TestOrderLocators.POPUP_BUTTON))
    )
    close_banner_button.click()
    yield driver
    driver.quit()