import allure
from selenium.webdriver.common.by import By

from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def set_name(self, name):
        name_field = self.find_element(locator=OrderLocators.FIELD_NAME)
        name_field.click()
        name_field.send_keys(name)

    def set_surname(self, surname):
        surname_field = self.find_element(locator=OrderLocators.FIELD_SURNAME)
        surname_field.click()
        surname_field.send_keys(surname)

    def set_adr(self, adress):
        adr_field = self.find_element(locator=OrderLocators.FIELD_ADRESS)
        adr_field.click()
        adr_field.send_keys(adress)

    def set_phone(self, phone):
        phone_field = self.find_element(locator=OrderLocators.FIELD_PHONE)
        phone_field.click()
        phone_field.send_keys(phone)

    @allure.step('Заполняем данные клиента')
    def set_client_data(self, name, surname, adress, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_adr(adress)
        self.set_phone(phone)

    @allure.step('Заполняем данные самоката (набор1)')
    def set_scooter_data_1(self):
        self.find_element(OrderLocators.FIELD_DATE).click()
        self.find_element(OrderLocators.FIELD_DATE_SELECT_31).click()
        self.find_element(OrderLocators.FIELD_DAYS).click()
        self.find_element(OrderLocators.FIELD_DAYS_SELECT_1).click()
        self.find_element(OrderLocators.FIELD_COLOR_1).click()

    @allure.step('Заполняем данные самоката (набор2)')
    def set_scooter_data_2(self):
        self.find_element(OrderLocators.FIELD_DATE).click()
        self.find_element(OrderLocators.FIELD_DATE_SELECT_02).click()
        self.find_element(OrderLocators.FIELD_DAYS).click()
        self.find_element(OrderLocators.FIELD_DAYS_SELECT_2).click()
        self.find_element(OrderLocators.FIELD_COLOR_2).click()

    @allure.step('Переходим на страницу статуса заказа, чтобы работать с логотипами')
    def order_approve_to_status_page(self):
        self.find_element(OrderLocators.ORDER_BUT_DOWN).click()
        self.find_element(OrderLocators.ORDER_BUT_YES).click()
        self.find_element(OrderLocators.CHECK_STATUS_BUTTON).click()

    @allure.step('Подтверждаем заказ')
    def order_approve(self):
        self.find_element(OrderLocators.ORDER_BUT_DOWN).click()
        self.find_element(OrderLocators.ORDER_BUT_YES).click()





