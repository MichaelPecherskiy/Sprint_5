import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators



@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.PERSONAL_AREA).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON).click()
    return driver


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
