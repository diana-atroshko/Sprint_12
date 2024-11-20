import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages import main_page, base_page
from pages.base_page import BasePage
from locators.logo_locators import LogosLocators
from locators.scooter_order_locators import TestOrderLocators
from pages.main_page import MainPage


class TestLogos:
    def test_logo_yandex(self, setup):
        driver = setup
        base_page = BasePage(setup)
        # Проверка логотипа Яндекса
        base_page.click_to_element(LogosLocators.LOGO_YANDEX)
        # Проверка нового окна
        driver.switch_to.window(driver.window_handles[1])
        assert (base_page.find_element_with_wait(LogosLocators.LOGO_DZEN).is_displayed() and driver.current_url == "https://dzen.ru/?yredirect=true")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_logo_scooter(self, setup):
        driver = setup
        base_page = BasePage(setup)
        base_page.click_to_element(LogosLocators.LOGO_SCOOTER)
        assert (base_page.find_element_with_wait(LogosLocators.HEADER_LOCATOR).is_displayed() and driver.current_url == "https://qa-scooter.praktikum-services.ru/")
