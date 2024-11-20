
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.scooter_order_locators import TestOrderLocators
from selenium.webdriver.common.by import By
from data import PARAMS
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.base_page import BasePage


class TestOrders:

    @pytest.mark.parametrize("order_data", [PARAMS[0]])
    def test_order_scooter_top_button(self, setup, order_data):
        driver = setup
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.scroll_to_element(TestOrderLocators.BUTTON_ORDER_ON_TOP)
        main_page.click_to_element(TestOrderLocators.BUTTON_ORDER_ON_TOP)

        order_page.set_order(*order_data)

        assert order_page.find_element_with_wait(TestOrderLocators.PLACED_ORDER).is_displayed()



    @pytest.mark.parametrize("order_data", [PARAMS[1]])
    def test_order_scooter_bottom_button(self, setup, order_data):
        driver = setup
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.scroll_to_element(TestOrderLocators.BUTTON_ORDER_DOWN)
        main_page.click_to_element(TestOrderLocators.BUTTON_ORDER_DOWN)

        order_page.set_order(*order_data)

        assert order_page.find_element_with_wait(TestOrderLocators.PLACED_ORDER).is_displayed()





