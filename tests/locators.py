from selenium.webdriver.common.by import By


class Locators:
    #register
    EMAIL = (By.XPATH, '(//input[@class="text input__textfield text_type_main-default"])[2]')
    PASSWORD = (By.XPATH, '(//div[@class="input pr-6 pl-6 input_type_password input_size_default"])/input')
    NAME_FIELD = (By.XPATH, '(//div[@class="input pr-6 pl-6 input_type_text input_size_default"])[1]/input')
    BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    #login
    LOGIN_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    LOGIN_EMAIL = (By.XPATH, '(//input[@class="text input__textfield text_type_main-default"])[1]')
    LOGIN_PASSWORD = (By.XPATH, '(//input[@class="text input__textfield text_type_main-default"])[2]')
    #others
    PERSONAL_AREA = (By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]')  #локатор личный кабинет
    REGISTRATION = (By.XPATH, '//a[@class="Auth_link__1fOlj"]') #локатор зарегестрироваться
    BUTTON_AUTH_ACCOUNT = (By.XPATH,
                           '(//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"])[1]') # локатор кнопки войти в аккаунт
    REG_BUTTON_PERSONAL_AREA = (By.XPATH, '(// a[@class ="Auth_link__1fOlj"])[1]') # локатор кнопки зарегистрироваться в там где войти в личный кабинет

    BREAD_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[1]")  # Кнопка скрола на Булки
    SAUCES_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[2]")  # Кнопка скрола на Соусы
    TOPPING_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[3]")  # Кнопка скрола на Начинки

    BREAD_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Булки')]")  # Поле с Названием Булки
    SAUCES_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Соусы')]")  # Поле с Названием Соусы
    TOPPING_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Начинки')]")  # Поле с Названием Начинки