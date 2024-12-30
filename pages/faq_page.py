import allure

from locators.faq_page_locators import Locators
from pages.base_page import BasePage


class FaqPage(BasePage):
    @allure.step('Проматываем страницу')
    def scroll_to_faq(self):
        element = self.find_element(locator=Locators.FAQ_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
