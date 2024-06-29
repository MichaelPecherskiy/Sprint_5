from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants


def test_logout(login):
    wait = WebDriverWait(login, 10)
    driver = login
    driver.find_element(*Locators.PRIVATE_AREA_LOCATOR).click()
    expected_url = Constants.URL_PROFILE
    wait.until(EC.url_to_be(Constants.URL_PROFILE))

    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")

    driver.find_element(*Locators.EXIT_BUTTON_LOCATOR).click() # локатор кнопки выход из аккаунта
    expected_url = Constants.URL_LOGIN
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")
