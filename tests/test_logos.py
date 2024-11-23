import pytest
import allure
from data import URL
from pages.main_page import MainPage


class TestLogos:
    @allure.title("Проверка логотипа Яндекса")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        driver.get(URL)
        main_page.close_banner(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        assert main_page.is_dzen_logo_displayed(), "Логотип Дзен не отображается или URL неправильный."


    @allure.title("Проверка логотипа Самоката")
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        driver.get(URL)
        main_page.close_banner(driver)
        main_page.click_scooter_logo()
        assert main_page.is_scooter_header_displayed(), "Заголовок Самокат не отображается или URL неправильный."
