from selenium.webdriver.common.by import By


class LogosLocators:
    LOGO_SCOOTER = [By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR"]
    LOGO_YANDEX = [By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI"]
    LOGO_DZEN = (By.CSS_SELECTOR, "a.dzen-layout--desktop-base-header__logoLink-2h")
    HEADER_LOCATOR = (By.CSS_SELECTOR, "div.Home_Header__iJKdX")