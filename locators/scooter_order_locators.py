from selenium.webdriver.common.by import By


class TestOrderLocators:
    BUTTON_ORDER_ON_TOP = [By.CSS_SELECTOR, ".Button_Button__ra12g"]
    BUTTON_ORDER_DOWN = [By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM"]
    NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    METRO_STATION = [By.XPATH, ".//*[contains(text(), '{}') and not(@class='some-hidden-class')]"]
    PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    DATE_DELIV = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    PERIOD = [By.XPATH, "//div[contains(@class, 'Dropdown-control')]"]
    PERIOD_TIME = [By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']"]
    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]
    CHECK_STATUS_BUTTON = [By.XPATH,"//button[contains(@class, 'Button_Button__ra12g') and text()='Посмотреть статус']"]
    BUTTON_ORDER_SCOOTER = [By.XPATH, "(//button[contains(text(), 'Заказать')])[2]"]
    PLACE_ORDER_QUESTION = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Хотите оформить заказ?')]"]
    BUTTON_YES = [By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Да']"]
    PLACED_ORDER = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]"]
    POPUP_BUTTON = [By.XPATH, "//button[contains(text(),'да все привыкли')]"]




