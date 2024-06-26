from tests.locators import Locators




def test_navigate_on_sections(login):
    driver = login

    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.SAUCES_LOCATOR).click()
    driver.find_element(*Locators.SAUCES_SECTION_LOCATOR).is_displayed()
    driver.find_element(*Locators.TOPPING_LOCATOR).click()
    driver.find_element(*Locators.TOPPING_SECTION_LOCATOR).is_displayed()
    driver.find_element(*Locators.BREAD_LOCATOR).click()
    driver.find_element(*Locators.BREAD_SECTION_LOCATOR).is_displayed()