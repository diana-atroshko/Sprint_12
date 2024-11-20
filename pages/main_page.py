import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.questions_locators import TestLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(TestLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(TestLocators.ANSWER_LOCATOR,num)
        self.scroll_to_element(TestLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)




