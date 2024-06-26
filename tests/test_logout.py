from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



def test_logout(login):
    driver = login
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click()
    expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
    WebDriverWait(driver, 5)

    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")

    driver.find_element(By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]').click() # локатор кнопки выход из аккаунта
    expected_url = "https://stellarburgers.nomoreparties.site/login"
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")
