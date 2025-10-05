import pytest
import allure
from pages.main_page import MainPage
from data import FAQ

faq_params = [(idx, answer) for idx, answer in enumerate(FAQ.expected_texts)]

class TestMainPage:
    @pytest.mark.parametrize('faq_index, expected_answer', faq_params)
    @allure.title("Проверка раскрытия текста ответа на вопрос FAQ №{faq_index}")
    @allure.description("При клике на стрелку вопроса должен отображаться корректный текст ответа.")
    def test_faq_answers(self, driver, faq_index, expected_answer):
        page = MainPage(driver)
        with allure.step(f"Открыть главную страницу и развернуть FAQ-вопрос №{faq_index+1}"):
            page.click_faq_question(faq_index)
        with allure.step("Проверить раскрытый текст ответа"):
            actual_answer = page.get_faq_answer_text(faq_index)
            assert expected_answer == actual_answer, f"Ожидали: {expected_answer}, получили: {actual_answer}"

    