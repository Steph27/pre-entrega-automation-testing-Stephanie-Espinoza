from pages.login_page import LoginPage
import pytest
from utils.reader import read_users_csv
from utils.logger import logger

@pytest.mark.parametrize(
        "data",read_users_csv())


def test_login(driver,data):
    try:
        logger.info("Iniciando prueba de login")
        login_page = LoginPage(driver) ##Se abre el navegador

        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina abierta correctamente")

        login_page.login(data["usuario"], data["password"])
        logger.info("Ingreso de credenciales")

        if data["tipo_usuario"] == "user_ok":
            assert "/inventory" in driver.current_url
            logger.info("Login exitoso")
        elif data["tipo_usuario"] == "user_error":
            error = login_page.obtener_mensaje_error()
            assert "Epic sadface" in error 
            logger.info("Prueba de mensaje de error valida")
    except Exception:
        logger.exception("Error durante la prueba de login")  
        raise      
        


