import allure
import pytest

from locators.faq_page_locators import Locators
from pages.faq_page import FaqPage


class TestFaqButton:
    @pytest.mark.parametrize('faq_button, faq_answer, answer_text', [
        [Locators.FAQ_BUTTON_1, Locators.FAQ_ANSWER_1, "Сутки — 400 рублей"],
        [Locators.FAQ_BUTTON_2, Locators.FAQ_ANSWER_2, "Пока что у нас так: один заказ"],
        [Locators.FAQ_BUTTON_3, Locators.FAQ_ANSWER_3, "Допустим, вы оформляете заказ на 8 мая"],
        [Locators.FAQ_BUTTON_4, Locators.FAQ_ANSWER_4, "Только начиная с завтрашнего дня. Но"],
        [Locators.FAQ_BUTTON_5, Locators.FAQ_ANSWER_5, "Но если что-то срочное"],
        [Locators.FAQ_BUTTON_6, Locators.FAQ_ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого"],
        [Locators.FAQ_BUTTON_7, Locators.FAQ_ANSWER_7, "Да, пока самокат не привезли. Штрафа"],
        [Locators.FAQ_BUTTON_8, Locators.FAQ_ANSWER_8, "Да, обязательно. Всем самокатов! И"]
    ])
    @allure.title('Тест выпадающего списка')
    @allure.description('Проверяю, что при клике на каждый из 8 вопросов открывается ответ на него ')
    def test_faq_button_opens_answer(self, driver,faq_button,faq_answer,answer_text ):
        faq_page = FaqPage(driver)
        faq_page.prepare_for_test()
        faq_page.scroll_to_faq()
        with allure.step('Нажимаем на вопрос'):
            faq_page.find_element(locator=faq_button).click()
        with allure.step('Проверяем, что ответ открылся'):
            visualcheck = faq_page.find_element(locator=faq_answer)
            assert answer_text in visualcheck.text

