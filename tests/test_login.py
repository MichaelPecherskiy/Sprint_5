from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators





def test_login_by_login_to_account(driver, wait):
    driver.find_element(*Locators.PRIVATE_AREA_LOCATOR).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PRIVATE_AREA_LOCATOR).click()
    expected_url = Constants.URL_PROFILE
    wait.until(EC.url_to_be(Constants.URL_PROFILE))
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")


def test_login_by_button_personal_area(driver, wait):
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PRIVATE_AREA_LOCATOR).click()
    expected_url = Constants.URL_PROFILE
    wait.until(EC.url_to_be(Constants.URL_PROFILE))
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")


def test_login_from_registration_form(driver, wait):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*Locators.REG_LOGIN_PAGE).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PRIVATE_AREA_LOCATOR).click()
    expected_url = Constants.URL_PROFILE
    wait.until(EC.url_to_be(Constants.URL_PROFILE))
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")


def test_login_from_password_recovery_form(driver, wait):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    driver.find_element(*Locators.FORGOT_PASSWORD_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.PRIVATE_AREA_LOCATOR).click()
    expected_url = Constants.URL_PROFILE
    wait.until(EC.url_to_be(Constants.URL_PROFILE))
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")
