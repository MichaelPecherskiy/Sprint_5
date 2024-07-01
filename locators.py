from selenium.webdriver.common.by import By


class Locators:
    #register
    EMAIL = (By.XPATH, "(//input[@type='text'])[2]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    NAME_FIELD = (By.XPATH, "(//input[@type='text'])[1]")
    BUTTON = (By.XPATH, "//button[contains(@Class, 'button_button')]") # Кнопка регистрации

    #login
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button')]") # Кнопка логина
    LOGIN_EMAIL = (By.XPATH, "//input[@type='text']")
    LOGIN_PASSWORD = (By.XPATH, "//input[contains(@type, 'password')]")

    REG_AUTH_LOCATOR = (By.XPATH, '//a[@class="Auth_link__1fOlj"]') # локатор зарегестрироваться на странице логина
    PRIVATE_AREA_LOCATOR = (By.XPATH, "//a[@href='/account']") # локатор личный кабинет
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '(// a[@class ="Auth_link__1fOlj"])[1]') # локатор в кнопке забыли пароль
    REG_LOGIN_PAGE = (By.XPATH, '(// a[@class ="Auth_link__1fOlj"])[1]')  # локатор кнопки зарегистрироваться на странице логина
    EXIT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'text')]") # кнопка выхода из аккаунта
    BUTTON_PRIVATE_ACC = (By.XPATH, "//a[@href='/account/profile']") # кнопка личного кабинета в настройках пользователя

    #others
    PERSONAL_AREA = (By.XPATH, "//a[@href='/account']")  #локатор личный кабинет
    REGISTRATION = (By.XPATH, '//a[@class="Auth_link__1fOlj"]') #локатор зарегестрироваться
    BUTTON_AUTH_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") # локатор кнопки войти в аккаунт
    REG_BUTTON_PERSONAL_AREA = (By.XPATH, '(// a[@class ="Auth_link__1fOlj"])[1]') # локатор кнопки зарегистрироваться в там где войти в личный кабинет

    BREAD_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[1]")  # Кнопка скрола на Булки
    SAUCES_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[2]")  # Кнопка скрола на Соусы
    TOPPING_LOCATOR = (By.XPATH, "(//span[@class= 'text text_type_main-default'])[3]")  # Кнопка скрола на Начинки

    BREAD_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Булки')]")  # Поле с Названием Булки
    SAUCES_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Соусы')]")  # Поле с Названием Соусы
    TOPPING_SECTION_LOCATOR = (By.XPATH, "//h2[contains(text(),'Начинки')]")  # Поле с Названием Начинки