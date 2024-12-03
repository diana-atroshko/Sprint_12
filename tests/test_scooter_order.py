import allure
import pytest
from data import PARAMS, URL
from pages.main_page import MainPage
from pages.order_page import OrderPage



class TestOrders:
    @pytest.mark.parametrize("order_data", [PARAMS[0]])
    @allure.title("Заказ самоката через верхнюю кнопку")
    def test_order_scooter_top_button(self,order_data, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_url(URL)
        main_page.close_banner()

        main_page.scroll_to_order_button("top")
        main_page.click_order_button("top")

        order_page.set_order(*order_data)

        assert order_page.is_order_placed_displayed()



    @pytest.mark.parametrize("order_data", [PARAMS[1]])
    @allure.title("Заказ самоката через нижнюю кнопку")
    def test_order_scooter_bottom_button(self,order_data, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_url(URL)
        main_page.close_banner()

        main_page.scroll_to_order_button("bottom")
        main_page.click_order_button("bottom")

        order_page.set_order(*order_data)

        assert order_page.is_order_placed_displayed()





