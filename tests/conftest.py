import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click() #локатор личный кабинет
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON).click()
    return driver
