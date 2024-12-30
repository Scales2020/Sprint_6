from urllib.error import URLError

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import driver
from constants import Constants
from locators.faq_page_locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    def go_to_site(self):
        self.driver.get(self.url)

    def check_cookie_button(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def find_element(self,locator, time=13):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def click_cookie(self):
        self.check_cookie_button(locator=Locators.COOKIE_BUTTON, time=5).click()

    @allure.step('Подготовка: открываем браузер, принимаем куки')
    def prepare_for_test(self):
        self.go_to_site()
        self.click_cookie()



