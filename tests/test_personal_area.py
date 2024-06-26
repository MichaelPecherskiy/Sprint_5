from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





def test_personal_area_click(login):
    driver = login
    driver.find_element(By.XPATH, '(//a[@class="AppHeader_header__link__3D_hX"])[last()]').click()
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo"]').click()
    expected_url = "https://stellarburgers.nomoreparties.site/"
    WebDriverWait(driver, 5)
    current_url = driver.current_url
    assert (expected_url, current_url, f"Expected URL: {expected_url}, but got: {current_url}")
