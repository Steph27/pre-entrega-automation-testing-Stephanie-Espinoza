from pages.login_page import LoginPage

def test_login_exitoso(driver):
    login_page = LoginPage(driver) ##Se abre el navegador

    driver.get("https://www.saucedemo.com/")

    login_page.login("standard_user", "secret_sauce")

    assert "/inventory" in driver.current_url


