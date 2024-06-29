from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from selenium.webdriver.support.ui import WebDriverWait


def test_personal_area_click(login):
    wait = WebDriverWait(login, 10)
    driver = login
    driver.find_element(*Locators.PRIVATE_AREA_LOCATOR).click()
    driver.find_element(*Locators.BUTTON_PRIVATE_ACC).click()
    expected_url = Constants.URL_MAIN_PAGE
    wait.until(EC.url_to_be(Constants.URL_MAIN_PAGE))
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")
