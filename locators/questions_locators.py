from selenium.webdriver.common.by import By

class TestLocators:
    QUESTION_LOCATOR = [By.XPATH, "//div[@id='accordion__heading-{}']"]
    ANSWER_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-{}']"]
    QUESTION_LOCATOR_TO_SCROLL = [By.ID, "accordion__heading-7"]

