import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента: {locator}')
    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step('Клик по элементу: {locator}')
    def click(self, locator):
        self.find(locator).click()

    @allure.step('Ввод текста "{text}" в поле: {locator}')
    def enter_text(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    @allure.step('Получение текста из элемента: {locator}')
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step('Скролл до элемента: {locator}')
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание, что URL становится {expected_url}')
    def wait_for_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

    @allure.step('Проверка отображения элемента: {locator}')
    def element_is_displayed(self, locator):
        return self.find(locator).is_displayed()
    
    @allure.step('Получение текущего URL страницы')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Ожидание открытия новой вкладки')
    def wait_for_new_tab(self, old_tabs):
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > len(old_tabs)
        )

    @allure.step('Переключение на последнюю вкладку')
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание, что текущий URL не about:blank')
    def wait_for_url_is_not_blank(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )

    @allure.step('Ожидание, что элемент кликабельный и клик по нему: {locator}')
    def wait_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Явное ожидание видимости и получение текста: {locator}')
    def wait_and_get_text(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)
    
    @allure.step('Двойной скролл до элемента и клик по нему: {locator}')
    def scroll_and_safe_click(self, locator):
        element = self.find(locator)
        # Скроллим к элементу и чуть сдвигаем вверх для компенсации флотирующих шапок
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("window.scrollBy(0, -90);")
        # Ждем, пока элемент действительно станет кликабельным
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Открытие страницы {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Получение списка открытых вкладок')
    def get_window_handles(self):
        return self.driver.window_handles
