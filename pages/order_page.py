import allure
import pytest
from locators.scooter_order_locators import TestOrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение данных заказа')
    def set_order(self, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        self.clear_element(TestOrderLocators.NAME)
        self.add_text_to_element(TestOrderLocators.NAME, first_name)

        self.clear_element(TestOrderLocators.LAST_NAME)
        self.add_text_to_element(TestOrderLocators.LAST_NAME, last_name)

        self.clear_element(TestOrderLocators.ADDRESS)
        self.add_text_to_element(TestOrderLocators.ADDRESS, address)

        self.click_to_element(TestOrderLocators.METRO)
        locator_formatted = self.format_locators(TestOrderLocators.METRO_STATION, metro_station)
        self.click_to_element(locator_formatted)

        self.clear_element(TestOrderLocators.PHONE)
        self.add_text_to_element(TestOrderLocators.PHONE, phone)

        self.click_to_element(TestOrderLocators.BUTTON_NEXT)

        self.click_to_element(TestOrderLocators.PERIOD)
        locator_period_formatted = self.format_locators(TestOrderLocators.PERIOD_TIME, rental_period)
        self.click_to_element(locator_period_formatted)


        self.click_to_element(TestOrderLocators.DATE_DELIV)
        self.clear_element(TestOrderLocators.DATE_DELIV)
        self.add_text_to_element(TestOrderLocators.DATE_DELIV, delivery_date)

        self.click_to_element(TestOrderLocators.BUTTON_ORDER_SCOOTER)
        self.find_element_with_wait(TestOrderLocators.PLACE_ORDER_QUESTION)
        self.click_to_element(TestOrderLocators.BUTTON_YES)


    @allure.step("Проверка отображения сообщения о заказе")
    def is_order_placed_displayed(self):
        return self.find_element_with_wait(TestOrderLocators.PLACED_ORDER).is_displayed()
