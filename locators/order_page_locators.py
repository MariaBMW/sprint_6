from selenium.webdriver.common.by import By

class OrderPageLocators:
    """" Форма Для кого самокат """
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")                                                         # Поле Имя в форме заказа
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")                                                  # Поле Фамилия в форме заказа
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")                               # Поле Адрес в форме заказа
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")                                              # Поле Станция метро в форме заказа
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")                           # Поле Телефон в форме заказа
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")                                                             # Кнопка Далее

    """ Форма Про аренду """
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")                                      # Поле для даты в форме заказа
    RENT_PERIOD_DROPDOWN_TOGGLE = (By.CSS_SELECTOR, "span.Dropdown-arrow")                                           # Кнопка для раскрытия выпадающего списка срока аренды
    RENT_PERIOD_ONE_DAY = (By.XPATH, ".//div[text()='сутки']")                                                       # Аренда на сутки
    RENT_PERIOD_TWO_DAYS = (By.XPATH, ".//div[text()='двое суток']")                                                 # Аренда на двое суток
    BLACK_SCOOTER = (By.ID, "black")                                                                                 # Чек-бокс черный жемчуг            
    GREY_SCOOTER = (By.ID, "grey")                                                                                   # Чек-бокс серая безысходность
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")                                    # Поле для комментария
    ORDER_BUTTON_FINISH = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")          # Кнопка Заказать под формой Про аренду

    """ Окно Хотите оформить заказ? """
    ORDER_YES_BUTTON = (By.XPATH, "//button[text() = 'Да']")                                                         # Кнопка Да в окне подтверждения

    """ Окно подтверждения успешного оформления заказа """
    STATUS_ORDER_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")                                         # Кнопка Посмотреть статус        



