from selenium.webdriver.common.by import By

class MainPageLocators:
    """" Шапка сайта """
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")                            # Логотип Яндекса в шапке сайта
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")                          # Логотип Самоката в шапке сайта
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']")      # Кнопка Заказать в шапке сайта

    """ Тело главной страницы """
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']")    # Кнопка Заказать в нижней части главной страницы

    """ Раздел Вопросы о важном """
    FAQ_QUESTIONS = [
        (By.ID, f"accordion__heading-{i}") for i in range(8)
    ]
    FAQ_ANSWERS = [
        (By.ID, f"accordion__panel-{i}") for i in range(8)
    ]



