from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants
from random_email import generate_email
from random_password import generate_random_password



def test_registration(driver):
    name = Constants.EMAIL
    driver.find_element(*Locators.PERSONAL_AREA).click()
    driver.find_element(*Locators.REG_AUTH_LOCATOR).click()
    driver.find_element(*Locators.NAME_FIELD).send_keys(name)
    driver.find_element(*Locators.EMAIL).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD).send_keys(generate_random_password())
    driver.find_element(*Locators.BUTTON).click()

    expected_url = Constants.URL_LOGIN
    WebDriverWait(driver, 5)
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")


def test_incorrect_password(driver):
    name = Constants.EMAIL
    driver.find_element(*Locators.PERSONAL_AREA).click()
    driver.find_element(*Locators.REG_AUTH_LOCATOR).click()
    driver.find_element(*Locators.NAME_FIELD).send_keys(name)
    driver.find_element(*Locators.EMAIL).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD).send_keys('123')
    driver.find_element(*Locators.BUTTON).click()

    message = driver.find_element(By.XPATH, '//p[@class="input__error text_type_main-default"]').text
    assert message == 'Некорректный пароль'
