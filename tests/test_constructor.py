from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



def test_click_constructor(login):
    driver = login
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click()
    expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
    WebDriverWait(driver, 5)
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")

