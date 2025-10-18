import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Users

def click_header(main_page):
    main_page.click_order_button_header()

def click_footer(main_page):
    main_page.click_order_button_footer()

test_data = [
    (Users.user_1, click_header, "Позитивный заказ: пользователь 1, кнопка в шапке"),
    (Users.user_2, click_footer, "Позитивный заказ: пользователь 2, кнопка внизу"),
]

@allure.suite("Оформление заказа самоката")
class TestOrder:
    
    @pytest.mark.parametrize('user, click_entry, desc', test_data)
    @allure.title("{desc}")
    @allure.description("Позитивный сценарий заказа самоката для разных пользователей через две точки входа.")
    def test_order_positive_flow(self, driver, user, click_entry, desc):
        main = MainPage(driver)
        with allure.step("Переход к форме заказа"):
            click_entry(main)
        order_page = OrderPage(driver)
        with allure.step("Заполнение личных данных"):
            order_page.fill_user_info(user)
        with allure.step("Заполнение данных по аренде"):
            order_page.fill_rent_info(user)
        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()
        with allure.step("Проверка окна успешного заказа"):
            assert order_page.is_order_success(), "Окно успешного заказа не появилось"