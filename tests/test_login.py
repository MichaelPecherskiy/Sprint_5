from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from tests.locators import Locators





def test_login_by_login_to_account(driver):
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click() # локатор личный кабинет
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click()
    expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
    WebDriverWait(driver, 5)
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")


def test_login_by_button_personal_area(driver):
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click() # локатор кнопки войти в аккаунт
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click()
    expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
    WebDriverWait(driver, 5)
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")


def test_login_from_registration_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, '(// a[@class ="Auth_link__1fOlj"])[1]').click() # локатор кнопки зарегистрироваться на странице логина
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click()
    expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
    WebDriverWait(driver, 5)
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")


def test_login_from_password_recovery_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    driver.find_element(By.XPATH, '(// a[@class ="Auth_link__1fOlj"])[1]').click() # локатор в кнопке забыли пароль где
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click()
    expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
    WebDriverWait(driver, 5)
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")
