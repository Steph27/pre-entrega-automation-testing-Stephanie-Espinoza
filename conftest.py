import pytest
from selenium import webdriver

import pytest_html
import pathlib
import base64

@pytest.fixture
def driver():
    #options = webdriver.EdgeOptions() ##En mi caso no hizo falta poner incognito
    #options.add_argument("--incognito")
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return{"x-api-key": "reqres_ae8f7a31c74e4df8a2e8c1cf4b12f98a"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield #Es el ultimo momento donde la prueba falló
    report = outcome.get_result()
    if report.when =="call" and report.failed:
        driver = item.funcargs.get("driver") 
        carpeta = pathlib.Path("reports/screenshots") #Almaceno la ruta de la carpeta donde quiero guardar las capturas
        carpeta.mkdir(parents=True, exist_ok=True) #Creo la carpeta si no existe
        archivo = carpeta / f"{item.name}.png" #Ruta donde se almacena la imagen

        driver.save_screenshot(str(archivo))
        imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8") #Codifico la imagen en base64
        report.extras = [
            pytest_html.extras.image(imagen, name="Screenshot") #Agrego una imagen dentro del reporte

        ] 
        

        
