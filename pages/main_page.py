import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step('Клик по кнопке "Заказать" в шапке')
    def click_order_button_header(self):
        # Делаем скролл и кликаем, чтобы шапка не перекрывала элемент
        button = self.find(MainPageLocators.ORDER_BUTTON_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("window.scrollBy(0, -100);")  # сверху шапка, смещаем
        self.wait_and_click(MainPageLocators.ORDER_BUTTON_HEADER)
        
    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_order_button_footer(self):
        button = self.find(MainPageLocators.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.wait_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Клик по вопросу FAQ №{index}')
    def click_faq_question(self, index):
        loc = MainPageLocators.FAQ_QUESTIONS[index]
        self.scroll_and_safe_click(loc)
        
    @allure.step('Получение текста ответа FAQ №{index}')
    def get_faq_answer_text(self, index):
        loc = MainPageLocators.FAQ_ANSWERS[index]
        return self.wait_and_get_text(loc)
        
        
    



