import allure
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL, ORDER_PAGE_URL

class TestLogoNavigation:

    @allure.title("Проверка перехода со страницы заказа на главную страницу по клику на логотип Самоката")
    @allure.description("Клик по логотипу Самоката должен вернуть пользователя на главную страницу.")
    def test_click_scooter_logo_navigate_to_main(self, driver):
        page = MainPage(driver)
        with allure.step("Открытие страницы заказа"):
            page.open(ORDER_PAGE_URL)
        with allure.step("Клик на логотип Самоката"):
            page.click_scooter_logo()
        with allure.step("Ожидание загрузки главной страницы и убеждение в переходе"):
            page.wait_for_url(MAIN_PAGE_URL)
            assert page.get_current_url() == MAIN_PAGE_URL, (
                f"Ожидался переход на главную страницу, но сейчас: {page.get_current_url()}"
            )

    @allure.title("Проверка перехода на страницу Дзена по клику на логотип Яндекса")
    @allure.description("Клик по логотипу Яндекса должен открыть Дзен в новой вкладке.")
    def test_click_yandex_logo_navigate_to_dzen(self, driver):
        page = MainPage(driver)
        with allure.step("Открытие страницы заказа"):
            page.open(ORDER_PAGE_URL)
        with allure.step("Запоминаем исходный список вкладок"):
            old_tabs = page.get_window_handles()
        with allure.step("Клик по логотипу Яндекса (должна открыться новая вкладка)"):
            page.click_yandex_logo()
        with allure.step("Ожидание открытия новой вкладки и переключение на неё"):
            page.wait_for_new_tab(old_tabs)
            page.switch_to_last_tab()
        with allure.step("Ожидание загрузки, что урл не about:blank"):
            page.wait_for_url_is_not_blank()
        with allure.step("Проверка, что открыт Дзен"):
            current_url = page.get_current_url()
            assert "dzen.ru" in current_url, f"Ожидался Dzen, а открыто: {current_url}"
            