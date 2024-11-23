import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.logo_locators import LogosLocators
from locators.questions_locators import TestLocators
from locators.scooter_order_locators import TestOrderLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Закрыть баннер')
    def close_banner(self, driver):
        close_banner_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((TestOrderLocators.POPUP_BUTTON)))
        close_banner_button.click()
        print("Баннер закрыт.")

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(TestLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(TestLocators.ANSWER_LOCATOR,num)
        self.scroll_to_element(TestLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_to_element(LogosLocators.LOGO_YANDEX)

    @allure.step("Клик по логотипу Скутера")
    def click_scooter_logo(self):
        self.click_to_element(LogosLocators.LOGO_SCOOTER)

    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[1])

    @allure.step("Закрытие текущего окна")
    def close_current_window(self):
        driver = self.driver
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    @allure.step("Проверка отображения логотипа Дзен")
    def is_dzen_logo_displayed(self):
        driver = self.driver
        return (self.find_element_with_wait(LogosLocators.LOGO_DZEN).is_displayed() and
                driver.current_url == "https://dzen.ru/?yredirect=true")

    @allure.step("Проверка отображения заголовка Самокат")
    def is_scooter_header_displayed(self):
        driver = self.driver
        return (self.find_element_with_wait(LogosLocators.HEADER_LOCATOR).is_displayed() and
                driver.current_url == "https://qa-scooter.praktikum-services.ru/")

    @allure.step("Прокрутка до кнопки заказа")
    def scroll_to_order_button(self, button_position):
        if button_position == "top":
            self.scroll_to_element(TestOrderLocators.BUTTON_ORDER_ON_TOP)
        elif button_position == "bottom":
            self.scroll_to_element(TestOrderLocators.BUTTON_ORDER_DOWN)

    @allure.step("Клик по кнопке заказа")
    def click_order_button(self, button_position):
        if button_position == "top":
            self.click_to_element(TestOrderLocators.BUTTON_ORDER_ON_TOP)
        elif button_position == "bottom":
            self.click_to_element(TestOrderLocators.BUTTON_ORDER_DOWN)