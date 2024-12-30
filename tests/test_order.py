from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators.order_locators import OrderLocators
from pages.order_page import OrderPage

import allure

class TestOrder:
    @allure.title('Тест создания заказа через верхнюю кнопку "Заказать" ')
    def test_order_from_up_button_completion_successful(self,driver):
        order_page = OrderPage(driver)
        order_page.prepare_for_test()
        with allure.step("Нажимаем на кнопку 'Заказать' наверху"):
            order_page.find_element(OrderLocators.ORDER_BUT_UP).click()
        order_page.set_client_data("Иван", "Быстрый", "Мойка,333", "89871231234")
        with allure.step("Выбираем станцию метро"):
            order_page.find_element(OrderLocators.FIELD_METRO).click()
            order_page.find_element(OrderLocators.FIELD_METRO_STATION_1).click()
        with allure.step("Переходим к следующему шагу"):
            order_page.find_element(OrderLocators.BUTTON_NEXT).click()
        order_page.set_scooter_data_1()
        order_page.order_approve()
        with allure.step("Проверяем успешность оформления заказа"):
            assert "Заказ оформлен" in order_page.find_element(OrderLocators.ORDER_SUCCESS).text

    @allure.title('Тест создания заказа через нижнюю кнопку "Заказать" ')
    def test_order_from_down_button_completion_successful(self,driver):
        order_page = OrderPage(driver)
        order_page.prepare_for_test()
        with allure.step("Нажимаем на кнопку 'Заказать' наверху"):
            order_page.find_element(OrderLocators.ORDER_BUT_DOWN).click()
        order_page.set_client_data("Пафнутий", "Шустрый", "Сюда,быстро", "89871231235")
        with allure.step("Выбираем станцию метро"):
            order_page.find_element(OrderLocators.FIELD_METRO).click()
            order_page.find_element(OrderLocators.FIELD_METRO_STATION_2).click()
        with allure.step("Переходим к следующему шагу"):
            order_page.find_element(OrderLocators.BUTTON_NEXT).click()
        order_page.set_scooter_data_2()
        order_page.order_approve()
        with allure.step("Проверяем успешность оформления заказа"):
            assert "Заказ оформлен" in order_page.find_element(OrderLocators.ORDER_SUCCESS).text

    @allure.title('Тест перехода со страницы заказа по логотипу "Самокат" на страницу Самоката ')
    def test_samokat_logo_goes_from_orderstatus_to_main(self, driver):
        order_page = OrderPage(driver)
        order_page.prepare_for_test()
        with allure.step("Нажимаем на кнопку 'Заказать' наверху"):
            order_page.find_element(OrderLocators.ORDER_BUT_DOWN).click()
        order_page.set_client_data("Пафнутий", "Шустрый", "Сюда,быстро", "89871231235")
        with allure.step("Выбираем станцию метро"):
            order_page.find_element(OrderLocators.FIELD_METRO).click()
            order_page.find_element(OrderLocators.FIELD_METRO_STATION_2).click()
        with allure.step("Переходим к следующему шагу"):
            order_page.find_element(OrderLocators.BUTTON_NEXT).click()
        order_page.set_scooter_data_2()
        order_page.order_approve_to_status_page()
        with allure.step('Нажимаем на лого Скутера'):
            order_page.find_element(OrderLocators.SCOOTER_BUTTON).click()
        with allure.step('Проверяем, что открылся сервис Самокат'):
            assert "Привезём его прямо к вашей двери" in order_page.find_element(OrderLocators.MAIN_PAGE_CHECK).text

    @allure.title('Тест перехода со страницы заказа по логотипу "Яндекс" на страницу Дзен ')
    def test_yandex_logo_goes_from_orderstatus_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.prepare_for_test()
        with allure.step("Нажимаем на кнопку 'Заказать' наверху"):
            order_page.find_element(OrderLocators.ORDER_BUT_DOWN).click()
        order_page.set_client_data("Пафнутий", "Шустрый", "Сюда,быстро", "89871231235")
        with allure.step("Выбираем станцию метро"):
            order_page.find_element(OrderLocators.FIELD_METRO).click()
            order_page.find_element(OrderLocators.FIELD_METRO_STATION_2).click()
        with allure.step("Переходим к следующему шагу"):
            order_page.find_element(OrderLocators.BUTTON_NEXT).click()
        order_page.set_scooter_data_2()
        order_page.order_approve_to_status_page()
        with allure.step('Нажимаем на лого Яндекса'):
            original_window = driver.current_window_handle
            order_page.find_element(OrderLocators.YA_BUTTON).click()
        with allure.step('Проверяем редирект на новую вкладку со страницей Дзена'):
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break
            WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Constants.EXPECTED_URL))
            current_page = driver.current_url
            assert current_page == Constants.EXPECTED_URL




