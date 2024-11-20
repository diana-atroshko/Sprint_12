import pytest
from pages.main_page import MainPage
from data import QUESTIONS_AND_ANSWERS

class TestMainPage:
    @pytest.mark.parametrize('num, result', QUESTIONS_AND_ANSWERS)

    def test_questions_and_answers(self, setup, num, result):
        main_page = MainPage(setup)
        answer_text = main_page.get_answer_text(num)
        assert answer_text == result

