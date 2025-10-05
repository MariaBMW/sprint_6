import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import Users

class OrderPage(BasePage):
    @allure.step('Заполнение данных пользователя')
    def fill_user_info(self, user):
        self.enter_text(OrderPageLocators.NAME_FIELD, user['name'])
        self.enter_text(OrderPageLocators.SURNAME_FIELD, user['surname'])
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, user['address'])
        self.choose_metro(user['subway'])
        self.enter_text(OrderPageLocators.PHONE_FIELD, user['phone'])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбор станции метро: {subway}')
    def choose_metro(self, subway):
        field = self.find(OrderPageLocators.METRO_FIELD)
        field.click()
        field.clear()
        field.send_keys(subway)
        # Поиск нужной станции в выпадающем списке 
        option_locator = (By.XPATH, f".//div[text()='{subway}']")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(option_locator)
        ).click()

    @allure.step('Заполнение данных по аренде')
    def fill_rent_info(self, user):
        self.enter_text(OrderPageLocators.DATE_FIELD, user['date'])
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN_TOGGLE)
        # Словарь для сопоставления срока аренды кнопке
        rent_days = {
        "сутки": OrderPageLocators.RENT_PERIOD_ONE_DAY,
        "двое суток": OrderPageLocators.RENT_PERIOD_TWO_DAYS
        }
        self.click(rent_days[user['rent_days_option']])
        # Словарь для сопоставления цвета самоката чекбоксу
        scooter_color = {
        "черный жемчуг": OrderPageLocators.BLACK_SCOOTER,
        "серая безысходность": OrderPageLocators.GREY_SCOOTER
        }
        self.click(scooter_color[user['color']])
        self.enter_text(OrderPageLocators.COMMENT_FIELD, user['comment'])
        self.click(OrderPageLocators.ORDER_BUTTON_FINISH)

    @allure.step('Подтверждение оформления заказа')
    def confirm_order(self):
        self.click(OrderPageLocators.ORDER_YES_BUTTON)

    @allure.step('Проверка успешного оформления заказа')
    def is_order_success(self):
        return self.element_is_displayed(OrderPageLocators.STATUS_ORDER_BUTTON)