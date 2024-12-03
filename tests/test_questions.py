import pytest
from pages.main_page import MainPage
from data import QUESTIONS_AND_ANSWERS, URL


class TestMainPage:
    @pytest.mark.parametrize('num, result', QUESTIONS_AND_ANSWERS)

    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_url(URL)
        main_page.close_banner()
        answer_text = main_page.get_answer_text(num)
        assert answer_text == result

